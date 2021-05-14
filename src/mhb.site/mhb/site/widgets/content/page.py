# -*- coding: utf-8 -*-
"""Module providing base widget"""
import uuid as uuid_tool

from AccessControl import Unauthorized
from Acquisition import aq_inner
from Products.Five import BrowserView
from ade25.widgets.interfaces import IContentWidgets
from plone import api
from plone.app.contenttypes.utils import replace_link_variables_by_paths


class WidgetADKPageSectionHeader(BrowserView):
    """ Base page header widget """

    def __call__(self,
                 widget_name='adk-page-section-header',
                 widget_type='adk-page-section-header',
                 widget_mode='view',
                 widget_data=None,
                 **kw):
        self.params = {
            'widget_name': widget_name,
            'widget_type': widget_type,
            'widget_mode': widget_mode,
            'widget_data': widget_data
        }
        return self.render()

    def render(self):
        return self.index()

    @property
    def edit_mode(self):
        if self.params['widget_mode'] == 'edit':
            return True
        return False

    @property
    def record(self):
        return self.params['widget_data']

    def has_content(self):
        if self.widget_content_record():
            return True
        return False

    def widget_uid(self):
        try:
            widget_id = self.record['id']
        except (KeyError, TypeError):
            widget_id = str(uuid_tool.uuid4())
        return widget_id

    def related_content_page(self):
        """Returns a list of brains of related items."""
        results = []
        catalog = api.portal.get_tool('portal_catalog')
        record = self.widget_content_record()
        if record:
            for rel in record['alias']:
                if rel.isBroken():
                    # skip broken relationsY
                    continue
                # query by path so we don't have to wake up any objects
                try:
                    brains = catalog(path={'query': rel.to_path, 'depth': 0})
                    results.append(brains[0])
                except (Unauthorized, IndexError):
                    print(rel.from_object.Title)
                    pass
        return results

    def has_related_content_page(self):
        return len(self.related_content_page()) > 0

    def widget_content_record(self):
        context = aq_inner(self.context)
        storage = IContentWidgets(context)
        content = storage.read_widget(self.widget_uid())
        return content

    def widget_content(self):
        widget_content = self.widget_content_record()
        data = {
            'headline': widget_content['headline'],
            'abstract': widget_content['abstract'],
            'public': widget_content['is_public']
        }
        return data


class WidgetADKPageSection(BrowserView):
    """ Page Section Widget """

    def __call__(self,
                 widget_name='adk-page-section',
                 widget_type='adk-page-section',
                 widget_mode='view',
                 widget_data=None,
                 **kw):
        self.params = {
            'widget_name': widget_name,
            'widget_type': widget_type,
            'widget_mode': widget_mode,
            'widget_data': widget_data
        }
        return self.render()

    def render(self):
        return self.index()

    @property
    def edit_mode(self):
        if self.params['widget_mode'] == 'edit':
            return True
        return False

    @property
    def record(self):
        return self.params['widget_data']

    def has_content(self):
        if self.widget_content_record():
            return True
        return False

    def widget_uid(self):
        try:
            widget_id = self.record['id']
        except (KeyError, TypeError):
            widget_id = str(uuid_tool.uuid4())
        return widget_id

    def display_cards(self):
        available = False
        for entry in self.widget_content_record():
            if entry.startswith('card_'):
                available = True
        return available

    def has_secondary_card(self):
        available = False
        if "card_text_secondary" in self.widget_content_record():
            available = True
        return available

    def widget_content_record(self):
        context = aq_inner(self.context)
        storage = IContentWidgets(context)
        content = storage.read_widget(self.widget_uid())
        return content

    def widget_content(self):
        widget_content = self.widget_content_record()
        data = {
            'headline': widget_content.get('headline'),
            'text': widget_content.get('text'),
            'display_cards': self.display_cards(),
            'card_icon': widget_content.get('card_icon'),
            'card_headline': widget_content.get('card_headline'),
            'card_text': widget_content.get('card_text'),
            'card_icon_secondary': widget_content.get('card_icon_secondary'),
            'card_secondary': self.has_secondary_card(),
            'card_headline_secondary': widget_content.get('card_headline_secondary'),
            'card_text_secondary': widget_content.get('card_text_secondary'),
            'public': widget_content['is_public']
        }
        return data


class WidgetADKPageHero(BrowserView):
    """ Base page hero unit with pictures """

    def __call__(self,
                 widget_name='adk-page-hero',
                 widget_type='adk-page-hero',
                 widget_mode='view',
                 widget_data=None,
                 **kw):
        self.params = {
            'widget_name': widget_name,
            'widget_type': widget_type,
            'widget_mode': widget_mode,
            'widget_data': widget_data
        }
        return self.render()

    def render(self):
        return self.index()

    @property
    def edit_mode(self):
        if self.params['widget_mode'] == 'edit':
            return True
        return False

    @property
    def record(self):
        return self.params['widget_data']

    def has_content(self):
        if self.widget_content_record():
            return True
        return False

    def widget_uid(self):
        try:
            widget_id = self.record['id']
        except (KeyError, TypeError):
            widget_id = str(uuid_tool.uuid4())
        return widget_id

    def widget_content_record(self):
        context = aq_inner(self.context)
        storage = IContentWidgets(context)
        content = storage.read_widget(self.widget_uid())
        return content

    @staticmethod
    def has_stored_image(image_object):
        context = image_object
        try:
            lead_img = context.image
        except AttributeError:
            lead_img = None
        if lead_img is not None:
            return True
        return False

    @staticmethod
    def _compute_aspect_ratio(scale_name):
        if scale_name.startswith('ratio'):
            return scale_name.split('-')[1].replace(':', '/')
        return scale_name

    def image_tag(self, image_uid):
        image = api.content.get(UID=image_uid)
        if self.has_stored_image(image):
            figure = image.restrictedTraverse('@@figure')(
                image_field_name='image',
                caption_field_name='image_caption',
                scale='ratio-4:3',
                aspect_ratio='4/3',
                lqip=True,
                lazy_load=True
            )
            return figure
        return None

    def widget_content(self):
        widget_content = self.widget_content_record()
        data = {
            'headline': widget_content['headline'],
            'abstract': widget_content['abstract'],
            'image': self.image_tag(widget_content['image']),
            'text': widget_content.get('text', None),
            'public': widget_content['is_public']
        }
        return data

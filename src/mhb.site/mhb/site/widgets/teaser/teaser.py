# -*- coding: utf-8 -*-
"""Module providing site widget"""
import uuid as uuid_tool

from Acquisition import aq_inner, aq_parent
from Products.Five import BrowserView
from ade25.base.interfaces import IContentInfoProvider
from ade25.widgets.interfaces import IContentWidgets
from plone import api
from plone.app.contenttypes.utils import replace_link_variables_by_paths


class ADKWidgetTeaserLinksInternal(BrowserView):
    """ Base widget used as placeholder """

    def __call__(self,
                 widget_name='adk-teaser-links-internal',
                 widget_type='adk-teaser-links-internal',
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
        if self.widget_content_items():
            return True
        return False

    def widget_uid(self):
        try:
            widget_id = self.record['id']
        except (KeyError, TypeError):
            widget_id = str(uuid_tool.uuid4())
        return widget_id

    def widget_item_nodes(self):
        context = aq_inner(self.context)
        ordered_nodes = list()
        storage = IContentWidgets(context)
        stored_widget = storage.read_widget(
            self.widget_uid()
        )
        if stored_widget:
            ordered_nodes = stored_widget["item_order"]
        return ordered_nodes

    def has_widget_item_nodes(self):
        return len(self.widget_item_nodes()) > 0

    def widget_item_content(self, widget_node):
        context = aq_inner(self.context)
        item_content = {
            "uid": widget_node
        }
        storage = IContentWidgets(context)
        stored_widget = storage.read_widget(
            self.widget_uid()
        )
        if stored_widget:
            content_items = stored_widget["items"]
            if content_items:
                try:
                    item_content.update(content_items[widget_node])
                except KeyError:
                    item_content = None
        return item_content

    def get_link_action(self, link):
        context = aq_inner(self.context)
        link_action = replace_link_variables_by_paths(context, link)
        return link_action

    def widget_content_items(self):
        return self.widget_item_nodes()

    def widget_custom_styles(self):
        if self.record and 'styles' in self.record:
            return self.record['styles']
        else:
            return None

    def widget_content_list_class(self):
        context = aq_inner(self.context)
        css_class = 'c-list c-list--{}'.format(
            context.UID())
        custom_styles = self.widget_custom_styles()
        if custom_styles:
            class_container = custom_styles['class_container']
            for class_name in class_container.split(' '):
                css_class = '{0} c-list--{1}'.format(
                    css_class,
                    class_name
                )
            if 'custom' in custom_styles:
                css_class = '{0} {1}'.format(
                    css_class,
                    custom_styles['custom']
                )
        return css_class

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

    def widget_content_record(self):
        context = aq_inner(self.context)
        storage = IContentWidgets(context)
        content = storage.read_widget(self.widget_uid())
        return content

    @staticmethod
    def widget_display(public):
        if not public and api.user.is_anonymous():
            return False
        return True

    def widget_content(self):
        widget_content = self.widget_content_record()
        data = {
            'title': widget_content.get('title'),
            'display': self.widget_display(widget_content.get('is_public', False)),

        }
        return data

    @staticmethod
    def time_stamp(item, date_time):
        content_info_provider = IContentInfoProvider(item)
        time_stamp = content_info_provider.time_stamp(date_time)
        return time_stamp

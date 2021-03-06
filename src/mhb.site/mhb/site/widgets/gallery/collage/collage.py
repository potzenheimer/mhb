# -*- coding: utf-8 -*-
"""Module providing site widget"""
import uuid as uuid_tool

from Acquisition import aq_inner
from Products.Five import BrowserView
from ade25.base.interfaces import IContentInfoProvider
from ade25.widgets.interfaces import IContentWidgets
from plone import api
from plone.app.contenttypes.utils import replace_link_variables_by_paths
from plone.app.textfield import IRichTextValue


class ADKWidgetGalleryCollage(BrowserView):
    """ Slider widget """

    def __call__(self,
                 widget_name='adk-collage',
                 widget_type='adk-collage',
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
                    node_content = content_items[widget_node]
                    if node_content['is_public']:
                        item_content.update(node_content)
                except KeyError:
                    item_content['is_public'] = False
        return item_content

    @staticmethod
    def widget_text_content(text):
        if IRichTextValue.providedBy(text):
            return text.output
        return text

    def get_link_action(self, link):
        context = aq_inner(self.context)
        link_action = replace_link_variables_by_paths(context, link)
        return link_action

    def widget_content_items(self):
        widget_nodes = list()
        item_nodes = self.widget_item_nodes()
        for item_node in item_nodes:
            node_content = self.widget_item_content(item_node)
            if node_content:
                image_uid = node_content.get('image', None)
                data = {
                    'uid': node_content.get('uid'),
                    'image': self.image_tag(image_uid),
                    'image_caption': node_content.get('image_caption'),
                    'image_alt': node_content.get('image_alt'),
                    'image_title': node_content.get('image_title'),
                    'public': node_content.get('is_public')
                }
                if data['public']:
                    widget_nodes.append(data)
        return widget_nodes

    def widget_custom_styles(self):
        if self.record and 'styles' in self.record:
            return self.record['styles']
        else:
            return None

    def widget_content_list_class(self):
        context = aq_inner(self.context)
        css_class = 'c-collage__items c-collage__items--{0}'.format(
            context.UID()
        )
        widget_nodes = self.widget_content_items()
        if widget_nodes:
            css_class = '{0} c-collage__items--{1}'.format(
                css_class,
                len(widget_nodes)
            )
        custom_styles = self.widget_custom_styles()
        if custom_styles:
            class_container = custom_styles['class_container']
            for class_name in class_container.split(' '):
                css_class = '{0} c-collage__items--{1}'.format(
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
    def time_stamp(item, date_time):
        content_info_provider = IContentInfoProvider(item)
        time_stamp = content_info_provider.time_stamp(date_time)
        return time_stamp

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

    def image_tag(self, image_uid):
        if image_uid:
            image = api.content.get(UID=image_uid)
            if self.has_stored_image(image):
                figure = image.restrictedTraverse('@@figure')(
                    image_field_name='image',
                    caption_field_name='image_caption',
                    scale='collage',
                    aspect_ratio='1/1',
                    lqip=True,
                    lazy_load=True,
                    css_class='o-figure--collage c-collage__figure',
                )
                return figure
        return None

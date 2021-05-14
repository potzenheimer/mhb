# -*- coding: utf-8 -*-
"""Module providing standalone content panel edit forms"""
from ade25.widgets.widgets.image.interfaces import asset_repository_path, \
    IAde25WidgetImageCover, IAde25WidgetImageBase, IAde25WidgetImageUpload, \
    IAde25WidgetImageRelated
from plone.app.textfield import RichText
from plone.app.z3cform.widget import LinkFieldWidget, RelatedItemsFieldWidget
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform import directives
from plone.namedfile import field as named_file
from z3c.relationfield import RelationChoice
from zope import schema
from zope.interface import Interface, provider

from ade25.panelpage import MessageFactory as _


@provider(IFormFieldProvider)
class IADKWidgetCollage(Interface):
    """ Content Widget Slider """
    pass


@provider(IFormFieldProvider)
class IADKWidgetCollageItem(Interface, IAde25WidgetImageBase):
    """ Image collection item

     Widget item with image upload and selection possibilities
     """

    #image = named_file.NamedBlobImage(
    #    title=_(u"Collage Image"),
    #    required=True
    #)
    #image_related = RelationChoice(
    #    title=_(u"Cover Image Select"),
    #    description=_(u"Select existing image in the asset repository"),
    #    required=False,
    #    default=None,
    #    vocabulary='ade25.widgets.vocabularies.ContentWidgetAssets'
    #)
    #directives.widget(
    #    'image_related',
    #    RelatedItemsFieldWidget,
    #    pattern_options={
    #        'recentlyUsed': False,
    #        'basePath':  asset_repository_path(),
    #        'path':  asset_repository_path(),
    #        'mode': 'auto',
    #        'favorites': [],
    #        'folderTypes': ['Folder', 'ade25.widgets.assetsfolder', ],
    #        'selectableTypes': ['Image'],
    #    }
    #)
    #image_caption = schema.TextLine(
    #    title=_(u"Image Copyright Information"),
    #    required=False
    #)
#
    #image_alt = schema.TextLine(
    #    title=_(u"Image Alt Text"),
    #    required=False
    #)
#
    #image_title = schema.TextLine(
    #    title=_(u"Image Title Text"),
    #    required=False
    #)

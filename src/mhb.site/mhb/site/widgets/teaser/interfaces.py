# -*- coding: utf-8 -*-
"""Module providing standalone content panel edit forms"""
from plone.app.textfield import RichText
from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform import directives as form, directives
from plone.app.z3cform.widget import LinkFieldWidget
from zope import schema
from zope.interface import Interface, provider
from plone.namedfile import field as named_file

from ade25.panelpage import MessageFactory as _


@provider(IFormFieldProvider)
class IADKWidgetTeaserLinksInternal(Interface):
    """ Content Widget Teaser Links internal """

    title = schema.TextLine(
        title=_("Teaser Headline"),
        required=False
    )


@provider(IFormFieldProvider)
class IADKWidgetLinkInternal(Interface):
    """ Content Panel Storage Slots """

    form.widget('icon', klass='js-choices-selector')
    icon = schema.Choice(
        title=_(u"Link Icon"),
        description=_(u"Select adequate icon for the linked section"),
        required=False,
        default='widget--tile',
        vocabulary='adk.site.vocabularies.InfoCardIconOptions'
    )
    headline = schema.TextLine(
        title=_("Teaser Title"),
        required=False
    )
    abstract = schema.Text(
        title=u"Teaser Abstract",
        description=_(u"Use the abstract to provide a short description of ."
                      u"the linked page content."),
        required=False,
    )
    image = named_file.NamedBlobImage(
        title=_(u"Cover Image"),
        required=True
    )
    image_caption = schema.TextLine(
        title=_(u"Cover Image Copyright Information"),
        required=False
    )
    text = RichText(
        title=_(u"Text"),
        required=False
    )
    directives.widget(link=LinkFieldWidget)
    link = schema.TextLine(
        title=_(u"Link"),
        description=_(u"Please select link target"),
        required=False,
    )

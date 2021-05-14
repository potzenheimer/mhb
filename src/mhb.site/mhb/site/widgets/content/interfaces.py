# -*- coding: utf-8 -*-
"""Module providing standalone content panel edit forms"""
from plone.app.textfield import RichText
from plone.app.z3cform.widget import LinkFieldWidget
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile import field as named_file
from zope import schema
from zope.interface import Interface, provider

from adk.site import _


@provider(IFormFieldProvider)
class IADKWidgetPageSection(Interface):
    """ Content Widget to display page section """

    headline = schema.TextLine(
        title=u"SectionHeadline",
        description=_(u"Please enter the page section headline (H2)."),
        required=False,
    )
    text = RichText(
        title=_(u"Text"),
        required=False
    )
    form.widget('card_icon', klass='js-choices-selector')
    card_icon = schema.Choice(
        title=_(u"Info Card 1: Icon"),
        description=_(u"Select adequate icon for the info card"),
        required=True,
        default='content--information',
        vocabulary='adk.site.vocabularies.InfoCardIconOptions'
    )
    card_headline = schema.TextLine(
        title=_(u"Info Card 1: Headline"),
        required=False
    )
    card_text = RichText(
        title=_(u"Info Card 1: Text"),
        required=False
    )

    form.widget('card_icon_secondary', klass='js-choices-selector')
    card_icon_secondary = schema.Choice(
        title=_(u"Info Card 2: Icon"),
        description=_(u"Select adequate icon for the info card"),
        required=True,
        default='content--information',
        vocabulary='adk.site.vocabularies.InfoCardIconOptions'
    )
    card_headline_secondary = schema.TextLine(
        title=_(u"Info Card 2: Headline"),
        required=False
    )

    card_text_secondary = RichText(
        title=_(u"Info Card 2: Text"),
        required=False
    )


@provider(IFormFieldProvider)
class IADKWidgetPageSectionHeader(Interface):
    """ Content Widget to display section header """

    headline = schema.TextLine(
        title=u"SectionHeadline",
        description=_(u"Please enter the page section headline (H2)."),
        required=False,
    )

    abstract = schema.Text(
        title=u"Section Abstract",
        description=_(u"Use the abstract to provide a short description of ."
                      u"the page content."),
        required=False,
    )


@provider(IFormFieldProvider)
class IADKWidgetPageHero(Interface):
    """ Content Widget to display page hero element """

    headline = schema.TextLine(
        title=u"Page Headline ",
        description=_(u"Please enter the page main headline (H1)."),
        required=False,
    )

    abstract = schema.Text(
        title=u"Page Abstract",
        description=_(u"Use the abstract to provide a short description of ."
                      u"the page content."),
        required=False,
    )
    text = RichText(
        title=_(u"Text"),
        required=False
    )

    image = named_file.NamedBlobImage(
        title=_(u"Cover Image"),
        required=True
    )
    image_caption = schema.TextLine(
        title=_(u"Cover Image Copyright Information"),
        required=False
    )
    image_alt = schema.TextLine(
        title=_(u"Cover Image Alt Text"),
        description=_(u"Use the image alt text for a short explaination of "
                      u"the image contents. This is SEO relevant information."),
        required=False
    )


@provider(IFormFieldProvider)
class IADKWidgetInfoCard(Interface):
    """ Info Card Widget """

    headline = schema.TextLine(
        title=_(u"Headline"),
        required=False
    )

    text = RichText(
        title=_(u"Text"),
        required=False
    )

    form.widget(link=LinkFieldWidget)
    link = schema.TextLine(
        title=_(u"Link"),
        description=_(u"Optional internal or external link that will be "
                      u"used as redirection target when section is accessed."
                      u"Logged in users will see the target link instead."),
        required=False,
    )

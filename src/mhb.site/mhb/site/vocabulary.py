# -*- coding: utf-8 -*-
"""Module providing panel page vocabularies"""
from binascii import b2a_qp

from zope.interface import implementer
from zope.schema. interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from adk.site import _


@implementer(IVocabularyFactory)
class InfoCardIconVocabularyFactory(object):

    def __call__(self, context):
        widgets = self.get_display_options()
        terms = [
            self.generate_simple_term(widget_key, widget_term)
            for widget_key, widget_term in widgets.items()
        ]
        return SimpleVocabulary(terms)

    @staticmethod
    def generate_simple_term(widget, widget_term):
        term = SimpleTerm(
            value=widget,
            token=b2a_qp(widget.encode('utf-8')),
            title=_(widget_term)
        )
        return term

    @staticmethod
    def get_display_options():
        display_options = {
            'content--information': _(u'Information'),
            'content--video': _(u'Video'),
            'content--alert': _(u'Alert'),
            'content--download': _(u'Download'),
            'content--chalkboard': _(u'Chalkboard and Teacher'),
            'content--school': _(u'School'),
            'content--calendar': _(u'Calendar'),
            'content--ribbon': _(u'Certificate'),
            'content--sun': _(u'Sun'),
            'content--bullhorn': _(u'Bullhorn'),
            'content--suitcase': _(u'Suitcase'),
        }
        return display_options


InfoCardIconVocabulary = InfoCardIconVocabularyFactory()

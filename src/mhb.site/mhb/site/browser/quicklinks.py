# -*- coding: utf-8 -*-
"""Module providing custom navigation strategy"""
from Acquisition import aq_inner
from ade25.panelpage.interfaces import IPanelPage
from plone import api
from plone.app.contenttypes.utils import replace_link_variables_by_paths
from plone.app.layout.viewlets import ViewletBase


class QuickLinksViewlet(ViewletBase):
    """ Context aware quick link navigation viewlet """

    def privacy_link(self):
        context = aq_inner(self.context)
        nav_root = api.portal.get_navigation_root(context)
        configured_links = api.content.find(
            context=nav_root,
            object_provides=IPanelPage,
            depth=1,
            review_state="published",
            is_promoted=True
        )
        try:
            link = configured_links[0]
            link_details = {
                'name': link.Title,
                'link': link.getURL()
            }
            return link_details
        except IndexError:
            return None

    def get_link_action(self, item):
        context = aq_inner(self.context)
        link = item.remoteUrl
        link_action = replace_link_variables_by_paths(context, link)
        return link_action

    def quick_links(self):
        context = aq_inner(self.context)
        nav_root = api.portal.get_navigation_root(context)
        configured_links = api.content.find(
            context=nav_root,
            object_provides=IPanelPage,
            depth=1,
            review_state="published",
            is_featured=True
        )
        quick_links = []
        for link in configured_links:
            link_details = {
                'name': link.Title,
                'link': link.getURL()
            }
            quick_links.append(link_details)
        return quick_links

    def available(self):
        return len(self.quick_links()) > 0

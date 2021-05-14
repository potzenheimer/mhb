# -*- coding: utf-8 -*-
"""Module providing helper views for widget management"""
import os
from Products.Five import BrowserView
from ade25.base.utils import get_filesystem_template
import json

from plone import api
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides


class SetupPackage(BrowserView):

    def __call__(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        return self.render()

    def render(self):
        return self.index()


class SetupPackageRunner(BrowserView):

    def __call__(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        return self.render()

    def render(self):
        scales = self._register_image_scales()
        return 'Registered {0} additional image scales'.format(scales)

    @staticmethod
    def package_image_scales():
        package_scales = (
            'ratio31',
        )
        image_scales = list()
        for scale_name in package_scales:
            scale_info_template = 'image-sizes-{0}.json'.format(scale_name)
            scale_info = get_filesystem_template(
                scale_info_template,
                os.path.abspath(os.path.join(
                    os.path.dirname(__file__),
                    os.pardir
                ))
            )
            try:
                scale_info_json = json.loads(scale_info)
                image_scales.append(json.dumps(scale_info_json))
            except ValueError:
                pass
        return image_scales

    def _register_image_scales(self):
        registry_settings = api.portal.get_registry_record(
            'ade25.base.responsive_image_scales'
        )
        image_scales = self.package_image_scales()
        idx = 0
        for scale in image_scales:
            if scale not in registry_settings:
                registry_settings.append(scale)
                idx += 1
        if idx > 0:
            api.portal.set_registry_record(
                'ade25.base.responsive_image_scales',
                registry_settings
            )
        return image_scales

    def _register_content_widgets(self):
        return

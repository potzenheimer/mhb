# -*- coding: utf-8 -*-
"""Module providing custom setup steps"""
import os

from ade25.base.utils import package_image_scales, register_image_scales
from ade25.widgets.utils import register_content_widgets

from mhb.site.config import PKG_WIDGETS
from mhb.site.config import PKG_IMAGE_SCALES


def setup_image_scales():
    image_scales = package_image_scales(PKG_IMAGE_SCALES, os.path.dirname(__file__))
    register_image_scales(image_scales)


def setup_content_widgets():
    content_widgets = PKG_WIDGETS
    register_content_widgets(content_widgets)


def setup_various(context):
    """
    @param context: Products.GenericSetup.context.DirectoryImportContext instance
    """

    # We check from our GenericSetup context whether we are running
    # add-on installation for your package or any other
    if context.readDataFile('mhb.site.marker.txt') is None:
        # Not your add-on
        return

    portal = context.getSite()

    setup_content_widgets()
    setup_image_scales()

# -*- coding: utf-8 -*-
# Module providing version specific upgrade steps
import logging
import os

from ade25.base.utils import register_image_scales, package_image_scales
from ade25.widgets.utils import register_content_widgets

from mhb.site.config import PKG_WIDGETS
from mhb.site.config import PKG_IMAGE_SCALES
from plone import api

default_profile = 'profile-mhb.site:default'
logger = logging.getLogger(__name__)


def upgrade_image_scales():
    image_scales = package_image_scales(PKG_IMAGE_SCALES, os.path.dirname(__file__))
    register_image_scales(image_scales)


def upgrade_content_widgets():
    content_widgets = PKG_WIDGETS
    register_content_widgets(content_widgets)


def upgrade_1001(setup):
    # setup.runImportStepFromProfile(default_profile, 'typeinfo')
    # Register project specific content widgets
    upgrade_content_widgets()
    # Register project specific image scales
    upgrade_image_scales()

# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from adk.site.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of adk.site into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if adk.site is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('adk.site'))

    def test_uninstall(self):
        """Test if adk.site is cleanly uninstalled."""
        self.installer.uninstallProducts(['adk.site'])
        self.assertFalse(self.installer.isProductInstalled('adk.site'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IHphWidgetsLayer is registered."""
        from adk.site.interfaces import IHphWidgetsLayer
        from plone.browserlayer import utils
        self.failUnless(IHphWidgetsLayer in utils.registered_layers())

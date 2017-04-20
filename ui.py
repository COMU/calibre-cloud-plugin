#!/usr/bin/env python2
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__   = 'GPL v3'
__copyright__ = '2017, Kerim Ölçer <kerimlcr@gmail.com>, Ali Güven Odabaşıoğlu <agaodabasioglu@gmail.com>'
__docformat__ = 'restructuredtext en'

if False:
    get_icons = get_resources = None

# The class that all interface action plugins must inherit from
from calibre.gui2.actions import InterfaceAction
from calibre_plugins.cloud_sync.main import DemoDialog, MainWindowForm



class InterfacePlugin(InterfaceAction):

    name = 'Cloud Sync'
    action_spec = ('Cloud Sync', None,
            'Cloud Sync', 'Ctrl+Shift+F1')

    def genesis(self):
        icon = get_icons('images/icon.png')
        self.qaction.setIcon(icon)
        self.qaction.triggered.connect(self.show_dialog)

    def show_dialog(self):
        self.mainwindow=MainWindowForm()
        self.mainwindow.show()
        """
        base_plugin_object = self.interface_action_base_plugin
        do_user_config = base_plugin_object.do_user_config
        d = DemoDialog(self.gui, self.qaction.icon(), do_user_config)
        d.show()
        """

    def apply_settings(self):
        from calibre_plugins.cloud_sync.config import prefs
        prefs


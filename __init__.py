#!/usr/bin/env python2
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__   = 'GPL v3'
__copyright__ = '2017, Kerim Ölçer <kerimlcr@gmail.com>, Ali Güven Odabaşıoğlu <agaodabasioglu@gmail.com>'
__docformat__ = 'restructuredtext en'

from calibre.customize import InterfaceActionBase

try:
    load_translations()
except NameError:
    pass # load_translations() added in calibre 1.9

class CloudSync(InterfaceActionBase):

    name                = 'Cloud Sync'
    description         = 'Cloud Sync'
    supported_platforms = ['linux']
    author              = 'Kerim Ölçer, Ali Güven Odabaşıoğlu'
    version             = (0, 0, 1)
    minimum_calibre_version = (0, 7, 53)


    actual_plugin = 'calibre_plugins.cloud_sync.ui:InterfacePlugin'

    def is_customizable(self):
        return False

    def config_widget(self):
        from calibre_plugins.cloud_sync.config import ConfigWidget
        return ConfigWidget()

    def save_settings(self, config_widget):
        config_widget.save_settings()

        ac = self.actual_plugin_
        if ac is not None:
            ac.apply_settings()



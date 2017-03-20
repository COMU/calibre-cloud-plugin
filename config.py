#!/usr/bin/env python2
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__   = 'GPL v3'
__copyright__ = '2017, Kerim Ölçer <kerimlcr@gmail.com>, Ali Güven Odabaşıoğlu <agaodabasioglu@gmail.com'
__docformat__ = 'restructuredtext en'

from PyQt5.Qt import QWidget, QHBoxLayout, QLabel, QLineEdit
import re
from calibre.utils.config import JSONConfig
from calibre.utils.config import config_dir


prefs = JSONConfig('plugins/cloud_sync')
prefs.defaults['username'] = 'username'
prefs.defaults['password'] = 'password'
prefs.defaults['librarypath'] = ''
prefs.defaults['language'] = ''

# Set defaults
language = 'Default'
books_path = config_dir + '/global.py'
myFile = open(books_path)
book_path = myFile.readlines()
for i in book_path:
    if re.search('library_path', i):
        file_path = i
    elif re.search('language =', i):
    	language = i
myFile.close()
file_path = file_path.split("u'")
file_path = file_path[1][0:len(file_path)-4]
language = language.split(" '")
language = language[1][0:2]
prefs.defaults['language'] = language
prefs.defaults['librarypath'] = file_path




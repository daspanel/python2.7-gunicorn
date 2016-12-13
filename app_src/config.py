#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""API Server

API server boilerplate using Connexion

 :copyright: (c) 2016, Abner G Jacobsen.
             All rights reserved.
 :license:   GNU General Public License v3, see LICENSE for more details.

"""

from __future__ import absolute_import, division, print_function
from __about__ import *


class ConfigSection(object):
    """Config object declaration."""
    def __init__(self, *args):
        self.__header__ = str(args[0]) if args else None

    def __repr__(self):
        if self.__header__ is None:
             return super(Struct, self).__repr__()
        return self.__header__

    def next(self):
        """ Fake iteration functionality.
        """
        raise StopIteration

    def __iter__(self):
        """ Fake iteration functionality.
        We skip magic attribues and Structs, and return the rest.
        """
        ks = self.__dict__.keys()
        for k in ks:
            if not k.startswith('__') and not isinstance(k, Struct):
                yield getattr(self, k)

    def __len__(self):
        """ Don't count magic attributes or Structs.
        """
        ks = self.__dict__.keys()
        return len([k for k in ks if not k.startswith('__')\
                    and not isinstance(k, Struct)])


# MySql configuration
mysql = ConfigSection("MySQL specific configuration")
mysql.user = 'api_server'
mysql.pwd = 'secret'
mysql.host = 'localhost'
mysql.port = 3306
mysql.database = 'API Server'

# Api configuration
api = ConfigSection("API Server API section config")
api.version = '0.1.0'
api.key = 'apikey'



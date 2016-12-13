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

__all__ = ('PETS_DB', 'PetsModel')

from .tinydb_json import PETS_DB, PetsModel



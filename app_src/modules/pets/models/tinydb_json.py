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

import os
from datetime import datetime
from tinydb_jsonorm import Database
from tinydb_jsonorm import TinyJsonModel
from tinydb_jsonorm import fields
from jsonmodels import models, validators

DATABASE_FILE = 'petsdb.json'

# Open pets database, creating it if not exists
PETS_DB = Database(DATABASE_FILE)

class PetTags(models.Base):
    id = fields.IntField(required=True)
    name = fields.StringField(required=True, validators=[validators.Length(1, 20)])

class PetsModel(TinyJsonModel):
    __tablename__ = "pets"
    id = fields.StringField(required=True, validators=[validators.Length(1, 255)])
    name = fields.StringField(required=True, validators=[validators.Length(1, 100)])
    animal_type = fields.StringField(required=True, validators=[validators.Length(1, 255)])
    tags = fields.ListField(['PetTags'])
    _last_update = fields.DateTimeField(required=True)
    _created_at = fields.DateTimeField(required=True)

    def __init__(self, *args, **kwargs):
        self._last_update = datetime.utcnow()
        self._created_at = self._last_update
        super(PetsModel, self).__init__(*args, **kwargs)

    class Meta:
        database = PETS_DB



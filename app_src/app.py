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
import connexion
import datetime
import logging

import config as CONFIG

logger = logging.getLogger(__name__)

# Create Connexion app
app = connexion.App(__name__)

# Trick: app.app is the Flask app object
flask_app = app.app
flask_app.logger_name = "api_server"

# Add api blueprints
app.add_api(
    'swagger/pets.yaml', base_path='/v1.0/pets'
)



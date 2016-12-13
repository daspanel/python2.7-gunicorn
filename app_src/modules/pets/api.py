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
import datetime
import logging

from connexion import request, NoContent

import config as CONFIG

logger = logging.getLogger(__name__)

from .models import PETS_DB, PetsModel

def get_pets(limit, animal_type=None):
    if not request.headers['X-Api-Key'] == CONFIG.api.key:
        return NoContent, 401
    all_recs = PetsModel.all()
    return [pet.to_struct() for pet in all_recs if not animal_type or pet.to_struct()['animal_type'] == animal_type][:limit]


def get_pet(pet_id):
    if not request.headers['X-Api-Key'] == CONFIG.api.key:
        return NoContent, 401
    try:
        pet_rec = PetsModel.get(PETS_DB.where("id") == pet_id)
        return pet_rec.to_struct(), 200
    except:
        logger.info('Pet not found: %s', pet_id)
        return {'message': 'Pet not found: {0}'.format(pet_id)}, 404


def post_pet(pet):
    if not request.headers['X-Api-Key'] == CONFIG.api.key:
        return NoContent, 401
    try:
        pet_rec = PetsModel.get(PETS_DB.where("id") == pet['id'])
        logger.info('Pet already exist: %s', pet['id'])
        return {'message': 'Pet already exist: {0}'.format(pet['id'])}, 400
    except:
        logger.info('Creating pet: %s', pet['id'])
        pet_rec = PetsModel(**pet)
        pet_rec.validate()
        pet_rec.insert()
        return NoContent, 201

def put_pet(pet_id, pet):
    if not request.headers['X-Api-Key'] == CONFIG.api.key:
        return NoContent, 401
    try:
        pet_rec = PetsModel.get(PETS_DB.where("id") == pet_id)
        pet_rec.name = pet['name']
        pet_rec.animal_type = pet['animal_type']
        pet_rec.tags = pet['tags']
        pet_rec.validate()
        pet_rec.save()
        return NoContent, 204
    except:
        logger.info('Pet not found: %s', pet_id)
        return {'message': 'Pet not found: {0}'.format(pet_id)}, 404

def delete_pet(pet_id):
    if not request.headers['X-Api-Key'] == CONFIG.api.key:
        return NoContent, 401
    try:
        pet_rec = PetsModel.get(PETS_DB.where("id") == pet_id)
        pet_rec.delete()
        return NoContent, 204
    except:
        logger.info('Pet not found: %s', pet_id)
        return {'message': 'Pet not found: {0}'.format(pet_id)}, 404




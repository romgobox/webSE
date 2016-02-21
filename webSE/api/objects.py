#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import request
from flask.views import MethodView
from webSE.api.model.objects import get_objects, add_object, update_object, del_object


class ObjectsAPI(MethodView):

    def get(self, object_id):
        if object_id is None:
            response = get_objects()
            return json.dumps(response)
        else:
            id = int(object_id)
            response = get_object(id)
            return json.dumps(response)

    def post(self):
        data = {}
        data['obj_desc'] = request.json['obj_desc']
        response = add_object(data)
        return json.dumps(response)

    def put(self, object_id):
        id = int(object_id)
        data = {}
        data['obj_desc'] = request.json['obj_desc']
        response = update_object(id, data)
        return json.dumps(response)

    def delete(self, object_id):
        id = int(object_id)
        response = del_object(id)
        return json.dumps(response)
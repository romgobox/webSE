#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import request
from flask.views import MethodView
from webSE.api.decorators import user_required
from webSE.api.model.meters_type import get_meters_type


class MetersTypeAPI(MethodView):
    decorators = [user_required]

    def get(self, meters_type_id):
        if meters_type_id is None:
            response = get_meters_type()
            return json.dumps(response)
        else:
            id = int(meters_type_id)
            response = get_meters_type(id)
            return json.dumps(response)

    def post(self):
        pass

    def put(self, protocol_id):
        pass

    def delete(self, protocol_id):
        pass
#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import request
from flask.views import MethodView
from webSE.api.decorators import user_required
from webSE.api.model.meters import get_meters, add_meter, update_meter, del_meter



class MetersAPI(MethodView):
    decorators = [user_required]

    def get(self, meter_id):
        if meter_id is None:
            response = get_meters()
            return json.dumps(response)
        else:
            id = int(meter_id)
            response = get_meter(id)
            return json.dumps(response)

    def post(self):
        data = {}
        data['type_id'] = int(request.json['type_id'])
        data['wh_adr'] = request.json['wh_adr']
        data['wh_num'] = request.json['wh_num']
        data['wh_pass'] = request.json['wh_pass']
        data['wh_desc'] = request.json['wh_desc']
        data['wh_KI'] = int(request.json['wh_KI'])
        data['wh_KU'] = int(request.json['wh_KU'])
        data['wh_IMPL'] = int(request.json['wh_IMPL'])
        data['wh_settings'] = request.json['wh_settings']
        data['object_id'] = int(request.json['object_id'])
        data['channel_id'] = int(request.json['channel_id'])
        data['is_active'] = int(request.json['is_active'])
        response = add_meter(data)
        return json.dumps(response)

    def put(self, meter_id):
        id = int(meter_id)
        data = {}
        data['type_id'] = int(request.json['type_id'])
        data['wh_adr'] = request.json['wh_adr']
        data['wh_num'] = request.json['wh_num']
        data['wh_pass'] = request.json['wh_pass']
        data['wh_desc'] = request.json['wh_desc']
        data['wh_KI'] = int(request.json['wh_KI'])
        data['wh_KU'] = int(request.json['wh_KU'])
        data['wh_IMPL'] = int(request.json['wh_IMPL'])
        data['wh_settings'] = request.json['wh_settings']
        data['object_id'] = int(request.json['object_id'])
        data['channel_id'] = int(request.json['channel_id'])
        data['is_active'] = int(request.json['is_active'])
        response = update_meter(id, data)
        return json.dumps(response)

    def delete(self, meter_id):
        id = int(meter_id)
        response = del_meter(id)
        return json.dumps(response)
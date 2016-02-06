#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import request
from flask.views import MethodView
from webSE.api.model.meters import get_meters, add_meter, update_meter, del_meter


class MetersAPI(MethodView):

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
        data['object_id'] = int(request.json['object_id'])
        data['wh_desc'] = request.json['wh_desc']
        data['protocol_id'] = int(request.json['protocol_id'])
        data['wh_num'] = request.json['wh_num']
        data['wh_adr'] = request.json['wh_adr']
        data['wh_pass'] = request.json['wh_pass']
        data['wh_settings'] = request.json['wh_settings']
        data['channel_id'] = int(request.json['channel_id'])
        response = add_meter(data)
        return json.dumps(response)

    def put(self, meter_id):
        id = int(meter_id)
        data = {}
        data['object_id'] = int(request.json['object_id'])
        data['wh_desc'] = request.json['wh_desc']
        data['protocol_id'] = int(request.json['protocol_id'])
        data['wh_num'] = request.json['wh_num']
        data['wh_adr'] = request.json['wh_adr']
        data['wh_pass'] = request.json['wh_pass']
        data['wh_settings'] = request.json['wh_settings']
        data['channel_id'] = int(request.json['channel_id'])
        response = update_meter(id, data)
        return json.dumps(response)

    def delete(self, meter_id):
        id = int(meter_id)
        response = del_meter(id)
        return json.dumps(response)
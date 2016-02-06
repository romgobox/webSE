#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import request
from flask.views import MethodView
from webSE.api.model.reports import get_protocols


class ProtocolsAPI(MethodView):

    def get(self, protocol_id):
        if protocol_id is None:
            response = get_protocols()
            return json.dumps(response)
        else:
            id = int(protocol_id)
            response = get_protocol(id)
            return json.dumps(response)

    def post(self):
        pass

    def put(self, protocol_id):
        pass

    def delete(self, protocol_id):
        pass
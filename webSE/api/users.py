#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import request, g
from flask.views import MethodView
from webSE.api.decorators import user_required
from webSE.api.model.users import get_user_info


class UserAPI(MethodView):
    decorators = [user_required]

    def get(self):
        user_id = g.user or None
        response = get_user_info(user_id)
        return json.dumps(response)

    def post(self):
        pass

    def put(self, channel_id):
        pass

    def delete(self, channel_id):
        pass
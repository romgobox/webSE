#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import request
from webSE import app
from webSE.api.model.reports import get_report_by_meter_id, get_report_diff_by_meter_id


@app.route('/reports/<int:param_num>/<int:meter_id>', methods=['POST'])
def report_by_meter_id(param_num, meter_id):
    param_num = int(param_num)
    meter_id = int(meter_id)
    data = {}
    data['param_num'] = param_num
    data['meter_id'] = meter_id
    data['date_start'] = request.json['date_start']
    data['date_end'] = request.json['date_end']
    report_type = request.json['report_type']
    if report_type == 'dates_list':
        response = get_report_by_meter_id(data)
    elif report_type == 'dates_diff':
        response = get_report_diff_by_meter_id(data)
    return json.dumps(response)
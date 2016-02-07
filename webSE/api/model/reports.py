#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
import datetime
from webSE.api.model import get_db

def get_report_by_meter_id(data):
    report_sql = '''
    SELECT 
        datetime_value, 
        value
    FROM
        webse.values
    WHERE
        meter_id={meter_id} 
        AND param_num={param_num} 
        AND datetime_value BETWEEN '{date_start}' AND '{date_end}'
    ORDER BY datetime_value
    '''.format(
            meter_id=data['meter_id'],
            param_num=data['param_num'],
            date_start=data['date_start'],
            date_end=data['date_end']
        )
    cur, con = get_db()
    cur.execute(report_sql)
    values = cur.fetchall()
    values_list = []
    for row in values:
        value = dict(row)
        value['datetime_value'] = value['datetime_value'].strftime('%d.%m.%y %H:%M:%S')
        values_list.append(value)
    return values_list

def get_report_diff_by_meter_id(data):
    report_sql = '''
    SELECT 
        datetime_value, 
        value
    FROM
        webse.values
    WHERE
        meter_id={meter_id} 
        AND param_num={param_num} 
        AND (datetime_value='{date_start}' OR datetime_value='{date_end}')
    ORDER BY datetime_value
    '''.format(
            meter_id=data['meter_id'],
            param_num=data['param_num'],
            date_start=data['date_start'],
            date_end=data['date_end']
        )
    cur, con = get_db()
    cur.execute(report_sql)
    values = cur.fetchall()
    values_list = []
    for row in values:
        value = dict(row)
        value['datetime_value'] = value['datetime_value'].strftime('%d.%m.%y %H:%M:%S')
        values_list.append(value)
    return values_list
    
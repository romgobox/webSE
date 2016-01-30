#! /usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import json

DATABASE = 'webSE/se.db'

def get_db(db):
    con = sqlite3.connect(db)
    con.row_factory=sqlite3.Row
    cur = con.cursor()
    return cur, con

def get_meters_info():
    meters_sql = '''
    SELECT wh.id, wh.wh_num, wh.wh_adr, wh.wh_desc, wh.wh_settings, wh.channel_id
    FROM meter as wh
    '''
    cur, con = get_db(DATABASE)
    cur.execute(meters_sql)
    data = cur.fetchall()
    meters = []
    for row in data:
        meter = dict(row)
        meter['wh_settings'] = json.loads(meter['wh_settings'])
        meters.append(meter)
    meters_info = json.dumps(meters)
    return meters_info

def get_meter_info(whID):
    meter_sql = '''
    SELECT wh.id, wh.wh_num, wh.wh_adr, wh.wh_desc, wh.wh_settings, wh.channel_id
    FROM meter as wh
    WHERE wh.id={id}
    '''.format(id=whID)

    cur, con = get_db(DATABASE)
    cur.execute(meter_sql)
    data = cur.fetchall()
    for row in data:
        meter = dict(row)
        meter['wh_settings'] = json.loads(meter['wh_settings'])
    meter_info = json.dumps(meter)
    return meter_info

def update_meter_info(whID, data):
    meter_sql = u'''
    UPDATE meter
    SET 
        wh_adr='{wh_adr}', 
        wh_num='{wh_num}', 
        wh_desc='{wh_desc}', 
        wh_settings='{wh_settings}', 
        channel_id={channel_id}
    WHERE id={id}
    '''.format(
            id=whID, 
            wh_adr=data['wh_adr'], 
            wh_num=data['wh_num'], 
            wh_desc=data['wh_desc'], 
            wh_settings=json.dumps(data['wh_settings']), 
            channel_id=data['channel_id'])

    response = {'status': u'Неопределено'}
    try:
        cur, con = get_db(DATABASE)
        cur.execute(meter_sql)
        con.commit()
        response['status'] = u'Сохранено'
    except Exception, e:
        response['status'] = u'Не сохранено. Причина: {e}'.format(e=e)
    return response

def add_meter(data):
    meter_sql = u'''
    INSERT INTO "meter" 
    VALUES(
        Null,
        '{wh_adr}', 
        '{wh_num}', 
        '777777', 
        '{wh_desc}', 
        '{wh_settings}', 
        'SE30X', 
        {channel_id})
    '''.format(
            wh_adr=data['wh_adr'], 
            wh_num=data['wh_num'], 
            wh_desc=data['wh_desc'], 
            wh_settings=json.dumps(data['wh_settings']), 
            channel_id=data['channel_id'])

    response = {'status': u'Неопределено'}
    try:
        cur, con = get_db(DATABASE)
        cur.execute(meter_sql)
        con.commit()
        data['id'] = cur.lastrowid
        response = data
        response['status'] = u'Добавлен новый прибор учета'
    except Exception, e:
        response['status'] = u'Прибор учета не добавлен. Причина: {e}'.format(e=e)
    return response

def delete_meter(id):
    meter_sql = u'''
    DELETE FROM meter
    WHERE id={id}
    '''.format(id=id)
    response = {'status': u'Неопределено'}
    try:
        cur, con = get_db(DATABASE)
        cur.execute(meter_sql)
        con.commit()
        response['status'] = u'Удален прибор учета'
    except Exception, e:
        response['status'] = u'Прибор учета не удален. Причина: {e}'.format(e=e)
    return response
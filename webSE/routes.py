#! /usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import MySQLdb
import MySQLdb.cursors
import json

# DATABASE = 'webSE/se.db'

# def get_db(db):
#     con = sqlite3.connect(db)
#     con.row_factory=sqlite3.Row
#     cur = con.cursor()
#     return cur, con
def get_db():
    con = MySQLdb.connect(host='localhost',
                            user='webse',
                            passwd='webse',
                            db='webse',
                            cursorclass=MySQLdb.cursors.DictCursor)
    cur = con.cursor()

    con.set_character_set('utf8')
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    return cur, con

# def get_meters_info():
#     # import pudb; pu.db
#     meters_sql = '''
#     SELECT 
#         wh.id, 
#         wh.wh_adr, 
#         wh.wh_num, 
#         wh.wh_pass, 
#         wh.object_id as obj_id,
#         wh.wh_desc, 
#         wh.wh_settings, 
#         wh.protocol_id as pr_id, 
#         wh.channel_id as ch_id
#     FROM 
#         meters wh
#     ORDER BY wh.object_id
#     '''
#     cur, con = get_db()
#     cur.execute(meters_sql)
#     meters = cur.fetchall()
#     meters_list = []
#     for row in meters:
#         # import pudb; pu.db
#         meter = dict(row)
#         meter['wh_settings'] = json.loads(meter['wh_settings'])
#         meters_list.append(meter)
#     return meters_list

# def get_objects_info():
#     # import pudb; pu.db
#     objects_sql = '''
#     SELECT
#         obj.id, 
#         obj.obj_desc
#     FROM
#         objects obj
#     '''
#     cur, con = get_db()
#     cur.execute(objects_sql)
#     objects = cur.fetchall()
#     objects_list = []
#     for row in objects:
#         object_row = dict(row)
#         objects_list.append(object_row)
#     return objects_list

def get_protocols_info():
    protocols_sql = '''
    SELECT 
        pr.id, 
        pr.pr_name, 
        pr.pr_desc, 
        pr.pr_settings
    FROM
        protocols pr
    '''
    cur, con = get_db()
    cur.execute(protocols_sql)
    protocols = cur.fetchall()
    protocols_list = []
    for row in protocols:
        protocol = dict(row)
        protocol['pr_settings'] = json.loads(protocol['pr_settings'])
        protocols_list.append(protocol)
    return protocols_list

# def get_channels_info():
#     channels_sql = '''
#     SELECT
#         ch.id, 
#         ch.ch_desc, 
#         ch.ch_ip, 
#         ch.ch_port,
#         ch.ch_settings
#     FROM
#         channels ch
#     '''
#     cur, con = get_db()
#     cur.execute(channels_sql)
#     channels = cur.fetchall()
#     channels_list = []
#     for row in channels:
#         channel = dict(row)
#         channel['ch_settings'] = json.loads(channel['ch_settings'])
#         channels_list.append(channel)
#     return channels_list

# def get_meter_info(whID):
#     meter_sql = '''
#     SELECT wh.id, wh.wh_num, wh.wh_adr, wh.wh_desc, wh.wh_settings, wh.channel_id
#     FROM meter as wh
#     WHERE wh.id={id}
#     '''.format(id=whID)

#     cur, con = get_db(DATABASE)
#     cur.execute(meter_sql)
#     data = cur.fetchall()
#     for row in data:
#         meter = dict(row)
#         meter['wh_settings'] = json.loads(meter['wh_settings'])
#     meter_info = json.dumps(meter)
#     return meter_info

# def update_meter_info(whID, data):
#     meter_sql = u'''
#     UPDATE meters
#     SET 
#         wh_adr='{wh_adr}', 
#         wh_num='{wh_num}', 
#         wh_pass='{wh_pass}', 
#         object_id={object_id},
#         wh_desc='{wh_desc}', 
#         wh_settings='{wh_settings}', 
#         protocol_id={protocol_id},
#         channel_id={channel_id}
#     WHERE id={id}
#     '''.format(
#             wh_adr=data['wh_adr'], 
#             wh_num=data['wh_num'], 
#             wh_pass=data['wh_pass'], 
#             object_id=data['obj_id'],
#             wh_desc=data['wh_desc'], 
#             wh_settings=json.dumps(data['wh_settings']), 
#             protocol_id=data['pr_id'],
#             channel_id=data['ch_id'],
#             id=whID)

#     response = {'status': u'Неопределено'}
#     try:
#         cur, con = get_db()
#         cur.execute(meter_sql)
#         con.commit()
#         response['status'] = u'Сохранено'
#     except Exception, e:
#         response['status'] = u'Не сохранено. Причина: {e}'.format(e=e)
#     return response

# def add_meter(data):
#     meter_sql = u'''
#     INSERT INTO meters 
#     VALUES(
#         Null,
#         '{wh_adr}', 
#         '{wh_num}',
#         '{wh_pass}',  
#         {object_id}, 
#         '{wh_desc}', 
#         '{wh_settings}', 
#         {protocol_id}, 
#         {channel_id})
#     '''.format(
#             wh_adr=data['wh_adr'], 
#             wh_num=data['wh_num'], 
#             wh_pass=data['wh_pass'], 
#             object_id=data['obj_id'],
#             wh_desc=data['wh_desc'], 
#             wh_settings=json.dumps(data['wh_settings']), 
#             protocol_id=data['pr_id'],
#             channel_id=data['ch_id'])

#     response = {'status': u'Неопределено'}
#     try:
#         cur, con = get_db()
#         cur.execute(meter_sql)
#         con.commit()
#         data['id'] = cur.lastrowid
#         response = data
#         response['status'] = u'Добавлен новый прибор учета'
#     except Exception, e:
#         response['status'] = u'Прибор учета не добавлен. Причина: {e}'.format(e=e)
#     return response

# def delete_meter(id):
#     meter_sql = u'''
#     DELETE FROM meters
#     WHERE id={id}
#     '''.format(id=id)
#     response = {'status': u'Неопределено'}
#     try:
#         cur, con = get_db()
#         cur.execute(meter_sql)
#         con.commit()
#         response['status'] = u'Удален прибор учета'
#     except Exception, e:
#         response['status'] = u'Прибор учета не удален. Причина: {e}'.format(e=e)
#     return response

# def update_channel_info(chID, data):
#     channel_sql = u'''
#     UPDATE channels
#     SET 
#         ch_desc='{ch_desc}', 
#         ch_ip='{ch_ip}', 
#         ch_port='{ch_port}', 
#         ch_settings='{ch_settings}'
#     WHERE id={id}
#     '''.format(
#             ch_desc=data['ch_desc'], 
#             ch_ip=data['ch_ip'], 
#             ch_port=data['ch_port'], 
#             ch_settings=json.dumps(data['ch_settings']),
#             id=chID)

#     response = {'status': u'Неопределено'}
#     try:
#         cur, con = get_db()
#         cur.execute(channel_sql)
#         con.commit()
#         response['status'] = u'Сохранено'
#     except Exception, e:
#         response['status'] = u'Не сохранено. Причина: {e}'.format(e=e)
#     return response

# def add_channel(data):
#     channel_sql = u'''
#     INSERT INTO channels 
#     VALUES(
#         Null, 
#         '{ch_desc}', 
#         '{ch_ip}', 
#         {ch_port},  
#         '{ch_settings}') 
#     '''.format(
#             ch_desc=data['ch_desc'], 
#             ch_ip=data['ch_ip'], 
#             ch_port=data['ch_port'], 
#             ch_settings=json.dumps(data['ch_settings'])) 

#     response = {'status': u'Неопределено'}
#     try:
#         cur, con = get_db()
#         cur.execute(channel_sql)
#         con.commit()
#         data['id'] = cur.lastrowid
#         response = data
#         response['status'] = u'Добавлен новый канал опроса'
#     except Exception, e:
#         response['status'] = u'Канал опроса не добавлен. Причина: {e}'.format(e=e)
#     return response

# def delete_channel(id):
#     channel_sql = u'''
#     DELETE FROM channels
#     WHERE id={id}
#     '''.format(id=id)
#     response = {'status': u'Неопределено'}
#     try:
#         cur, con = get_db()
#         cur.execute(channel_sql)
#         con.commit()
#         response['status'] = u'Удален канал опроса'
#     except Exception, e:
#         response['status'] = u'Канал опроса не удален. Причина: {e}'.format(e=e)
#     return response

# def update_object_info(objID, data):
#     object_sql = u'''
#     UPDATE objects
#     SET 
#         obj_desc='{obj_desc}'
#     WHERE id={id}
#     '''.format(
#             obj_desc=data['obj_desc'], 
#             id=objID)

#     response = {'status': u'Неопределено'}
#     try:
#         cur, con = get_db()
#         cur.execute(object_sql)
#         con.commit()
#         response['status'] = u'Сохранено'
#     except Exception, e:
#         response['status'] = u'Не сохранено. Причина: {e}'.format(e=e)
#     return response

# def add_object(data):
#     object_sql = u'''
#     INSERT INTO objects 
#     VALUES(
#         Null, 
#         '{obj_desc}') 
#     '''.format(obj_desc=data['obj_desc']) 

#     response = {'status': u'Неопределено'}
#     try:
#         cur, con = get_db()
#         cur.execute(object_sql)
#         con.commit()
#         data['id'] = cur.lastrowid
#         response = data
#         response['status'] = u'Добавлен новый объект учета'
#     except Exception, e:
#         response['status'] = u'Объект учета не добавлен. Причина: {e}'.format(e=e)
#     return response

# def delete_object(id):
#     object_sql = u'''
#     DELETE FROM objects
#     WHERE id={id}
#     '''.format(id=id)
#     response = {'status': u'Неопределено'}
#     try:
#         cur, con = get_db()
#         cur.execute(object_sql)
#         con.commit()
#         response['status'] = u'Удален объект учета'
#     except Exception, e:
#         response['status'] = u'Объект учета не удален. Причина: {e}'.format(e=e)
#     return response

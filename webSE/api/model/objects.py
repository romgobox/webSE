#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from webSE.api.model import get_db

def get_objects():
    objects_sql = '''
    SELECT
        obj.id, 
        obj.obj_desc
    FROM
        objects obj
    '''
    cur, con = get_db()
    cur.execute(objects_sql)
    objects = cur.fetchall()
    objects_list = []
    for row in objects:
        object_row = dict(row)
        objects_list.append(object_row)
    return objects_list

def add_object(data):
    object_sql = u'''
    INSERT INTO objects 
    VALUES(
        Null, 
        '{obj_desc}') 
    '''.format(obj_desc=data['obj_desc']) 

    response = {'status': u'Неопределено'}
    try:
        cur, con = get_db()
        cur.execute(object_sql)
        con.commit()
        data['id'] = cur.lastrowid
        response = data
        response['status'] = u'Добавлен новый объект учета'
    except Exception, e:
        response['status'] = u'Объект учета не добавлен. Причина: {e}'.format(e=e)
    return response

def update_object(objID, data):
    object_sql = u'''
    UPDATE objects
    SET 
        obj_desc='{obj_desc}'
    WHERE id={id}
    '''.format(
            obj_desc=data['obj_desc'], 
            id=objID)

    response = {'status': u'Неопределено'}
    try:
        cur, con = get_db()
        cur.execute(object_sql)
        con.commit()
        response['status'] = u'Сохранено'
    except Exception, e:
        response['status'] = u'Не сохранено. Причина: {e}'.format(e=e)
    return response

def del_object(id):
    object_sql = u'''
    DELETE FROM objects
    WHERE id={id}
    '''.format(id=id)
    response = {'status': u'Неопределено'}
    try:
        cur, con = get_db()
        cur.execute(object_sql)
        con.commit()
        response['status'] = u'Удален объект учета'
    except Exception, e:
        response['status'] = u'Объект учета не удален. Причина: {e}'.format(e=e)
    return response
#! /usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
# import sqlite3
import json
# from seweb.config import DATABASE
# from SE30x.protocol import SE30X
# from SE30x.tcp_channel import TCPChannel as TCP

# app = Flask(__name__)
from webSE import app
from webSE.routes import get_meters_info, get_objects_info, get_protocols_info, get_channels_info, \
                         get_meter_info, update_meter_info, \
                         add_meter, delete_meter, \
                         update_channel_info, add_channel, delete_channel, \
                         add_object, update_object_info, delete_object

@app.route('/')
def hello():
    # cur = get_meters()
    return render_template('index.html')

################################################################################
# Main API
################################################################################
@app.route('/meters', methods=['GET'])
def get_meters():
    if request.method == 'GET':
        meters_info = get_meters_info()
        return json.dumps(meters_info)

@app.route('/objects', methods=['GET'])
def get_objects():
    if request.method == 'GET':
        objects_info = get_objects_info()
        return json.dumps(objects_info)

@app.route('/protocols', methods=['GET'])
def get_protocols():
    if request.method == 'GET':
        protocols_info = get_protocols_info()
        return json.dumps(protocols_info)

@app.route('/channels', methods=['GET'])
def get_channels():
    if request.method == 'GET':
        channels_info = get_channels_info()
        return json.dumps(channels_info)

################################################################################
# Meter API
################################################################################
@app.route('/meterinfo/<int:id>', methods=['POST', 'GET'])
def meter_info(id):
    # import pudb; pu.db
    if request.method == 'GET':
        # cur = get_meter_info(id)
        meter_info = get_meter_info(id)
        # return render_template('modal/whinfo.html', cur=cur)
        return meter_info
    elif request.method == 'POST':
        # import pudb; pu.db
        data = {}
        data['obj_id'] = int(request.json['obj_id'])
        data['wh_desc'] = request.json['wh_desc']
        data['pr_id'] = int(request.json['pr_id'])
        data['wh_num'] = request.json['wh_num']
        data['wh_adr'] = request.json['wh_adr']
        data['wh_pass'] = request.json['wh_pass']
        data['wh_settings'] = request.json['wh_settings']
        data['ch_id'] = int(request.json['ch_id'])
        response = update_meter_info(id, data)
        return json.dumps(response)

@app.route('/addmeter', methods=['PUT'])
def meter_add():
    if request.method == 'PUT':
        data = {}
        data['obj_id'] = int(request.json['obj_id'])
        data['wh_desc'] = request.json['wh_desc']
        data['pr_id'] = int(request.json['pr_id'])
        data['wh_num'] = request.json['wh_num']
        data['wh_adr'] = request.json['wh_adr']
        data['wh_pass'] = request.json['wh_pass']
        data['wh_settings'] = request.json['wh_settings']
        data['ch_id'] = int(request.json['ch_id'])
        response = add_meter(data)
        return json.dumps(response)

@app.route('/delmeter/<int:id>', methods=['POST'])
def meter_delete(id):
    if request.method == 'POST':
        response = delete_meter(id)
        return json.dumps(response)

################################################################################
# Channel API
################################################################################
@app.route('/channelinfo/<int:id>', methods=['POST', 'GET'])
def channel_info(id):
    if request.method == 'GET':
        pass
        # meter_info = get_meter_info(id)
        # return meter_info
    elif request.method == 'POST':
        data = {}
        data['ch_desc'] = request.json['ch_desc']
        data['ch_ip'] = request.json['ch_ip']
        data['ch_port'] = int(request.json['ch_port'])
        data['ch_settings'] = request.json['ch_settings']
        response = update_channel_info(id, data)
        return json.dumps(response)

@app.route('/addchannel', methods=['PUT'])
def channel_add():
    if request.method == 'PUT':
        data = {}
        data['ch_desc'] = request.json['ch_desc']
        data['ch_ip'] = request.json['ch_ip']
        data['ch_port'] = int(request.json['ch_port'])
        data['ch_settings'] = request.json['ch_settings']
        response = add_channel(data)
        return json.dumps(response)

@app.route('/delchannel/<int:id>', methods=['POST'])
def channel_delete(id):
    if request.method == 'POST':
        response = delete_channel(id)
        return json.dumps(response)

################################################################################
# Object API
################################################################################
@app.route('/objectinfo/<int:id>', methods=['POST', 'GET'])
def object_info(id):
    if request.method == 'GET':
        pass
        # meter_info = get_meter_info(id)
        # return meter_info
    elif request.method == 'POST':
        data = {}
        data['obj_desc'] = request.json['obj_desc']
        response = update_object_info(id, data)
        return json.dumps(response)

@app.route('/addobject', methods=['PUT'])
def object_add():
    if request.method == 'PUT':
        data = {}
        data['obj_desc'] = request.json['obj_desc']
        response = add_object(data)
        return json.dumps(response)

@app.route('/delobject/<int:id>', methods=['POST'])
def object_delete(id):
    if request.method == 'POST':
        response = delete_object(id)
        return json.dumps(response)

# @app.route('/get_val', methods=['GET', 'POST'])
# def get_val():
#     # import pdb; pdb.set_trace()
#     try:
#         whID = request.json['id']
#     except Exception, e:
#         whID = 1
#         print e
#     wh_sql = '''
#     SELECT wh.wh_adr, ch.ip_adr, ch.ip_port 
#     FROM meter as wh, channels as ch 
#     WHERE wh.id=%s AND wh.channel_id=ch.id
#     ''' % whID
    
#     con = sqlite3.connect(DATABASE)
#     cur = con.cursor()
#     cur.execute(wh_sql)
#     con.commit()

#     for c in cur.fetchall():
#         whData = dict(adr=c[0], ip=c[1], port=c[2])
    
#     channel = TCP(attempt = 3,  whTimeout=15)
#     se = SE30X(channel)
#     conn = channel.connect(address=whData['ip'], port=whData['port'])

#     if se.whAuth(whData['adr'], 777777):
#         whNumber = se.whNum(whData['adr']) or u'не удалось прочитать номер'
#         PE = se.whFixMonth(whData['adr'], date='11.15')
#         se.whLogOut(whData['adr'])
        
#         whValue = dict(adr=whData['adr'], whnum=whNumber, sum=round(PE['Sum'], 2), \
#                                                     T1=round(PE['T1'], 2), T2=round(PE['T2'], 2))
        
#         '''
#         dict = [
#             {whAdr:'275',
#             whNum:'00923',
#             summ:'189.090'

#             }
#         ]
#         '''
#     else:
#         whValue = dict(adr=whData['adr'], whnum=u'не удалось прочитать номер', \
#                         sum=u'нет данных', T1=u'нет данных', T2=u'нет данных')
#     return jsonify(whValue)

if __name__=='__main__':
    app.run(debug=True)
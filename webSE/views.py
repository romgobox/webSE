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
from webSE.routes import get_meters_info, get_meter_info, update_meter_info, add_meter, delete_meter

@app.route('/')
def hello():
    # cur = get_meters()
    return render_template('index.html')

@app.route('/meters', methods=['GET'])
def get_meters():
    if request.method == 'GET':
        meters_info = get_meters_info()
        return meters_info

@app.route('/meterinfo/<int:id>', methods=['POST', 'GET'])
def meter_info(id):
    # import pudb; pu.db
    if request.method == 'GET':
        # cur = get_meter_info(id)
        meter_info = get_meter_info(id)
        # return render_template('modal/whinfo.html', cur=cur)
        return meter_info
    elif request.method == 'POST':
        data = {}
        data['wh_desc'] = request.json['wh_desc']
        data['wh_num'] = request.json['wh_num']
        data['wh_adr'] = request.json['wh_adr']
        data['wh_settings'] = request.json['wh_settings']
        data['channel_id'] = int(request.json['channel_id'])
        response = update_meter_info(id, data)
        return json.dumps(response)

@app.route('/addmeter', methods=['PUT'])
def meter_add():
    if request.method == 'PUT':
        data = {}
        data['wh_desc'] = request.json['wh_desc']
        data['wh_num'] = request.json['wh_num']
        data['wh_adr'] = request.json['wh_adr']
        data['wh_settings'] = request.json['wh_settings']
        data['channel_id'] = int(request.json['channel_id'])
        response = add_meter(data)
        return json.dumps(response)

@app.route('/delmeter/<int:id>', methods=['POST'])
def meter_delete(id):
    if request.method == 'POST':
        response = delete_meter(id)
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
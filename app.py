#! /usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
import sqlite3
import json
from seweb.config import DATABASE
from SE30x.protocol import SE30X
from SE30x.tcp_channel import TCPChannel as TCP

app = Flask(__name__)


@app.route('/')
def hello():
    meters_sql = '''
    SELECT wh.id, wh.wh_num, wh.wh_adr, wh.wh_desc, ch.ip_adr, ch.ip_port 
    FROM meter as wh, channels as ch 
    WHERE wh.channel_id=ch.id
    '''

    con = sqlite3.connect(DATABASE)
    cur = con.cursor()

    cur.execute(meters_sql)
    con.commit()

    return render_template('index.html', cur=cur)

@app.route('/meter/<int:id>')
def get_meter_id(id):
    wh_sql = '''
    SELECT wh.wh_adr, ch.ip_adr, ch.ip_port 
    FROM meter as wh, channels as ch 
    WHERE wh.id=%s AND wh.channel_id=ch.id
    ''' % id

    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute(wh_sql)
    con.commit()

    for c in cur.fetchall():
        whData = dict(adr=c[0], ip=c[1], port=c[2])

@app.route('/get_val', methods=['GET', 'POST'])
def get_val():
    # import pdb; pdb.set_trace()
    try:
        whID = request.json['id']
    except Exception, e:
        whID = 1
        print e
    wh_sql = '''
    SELECT wh.wh_adr, ch.ip_adr, ch.ip_port 
    FROM meter as wh, channels as ch 
    WHERE wh.id=%s AND wh.channel_id=ch.id
    ''' % whID
    
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute(wh_sql)
    con.commit()

    for c in cur.fetchall():
        whData = dict(adr=c[0], ip=c[1], port=c[2])
    
    channel = TCP(attempt = 3,  whTimeout=15)
    se = SE30X(channel)
    conn = channel.connect(address=whData['ip'], port=whData['port'])

    if se.whAuth(whData['adr'], 777777):
        whNumber = se.whNum(whData['adr']) or u'не удалось прочитать номер'
        PE = se.whFixMonth(whData['adr'], date='11.15')
        se.whLogOut(whData['adr'])
        
        whValue = dict(adr=whData['adr'], whnum=whNumber, sum=round(PE['Sum'], 2), \
                                                    T1=round(PE['T1'], 2), T2=round(PE['T2'], 2))
        
        '''
        dict = [
            {whAdr:'275',
            whNum:'00923',
            summ:'189.090'

            }
        ]
        '''
    else:
        whValue = dict(adr=whData['adr'], whnum=u'не удалось прочитать номер', \
                        sum=u'нет данных', T1=u'нет данных', T2=u'нет данных')
    return jsonify(whValue)

if __name__=='__main__':
    app.run(debug=True)
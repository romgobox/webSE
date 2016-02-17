#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import gevent.monkey
# gevent.monkey.patch_socket()

# import logging
# import json
# from kombu import Connection, Exchange, Queue, Consumer
# from SE30x.algorithm import Algorithm
# logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-4s [%(asctime)s] %(message)s', level = logging.DEBUG)
from requestd.alg_worker import main



if __name__ == '__main__':
    main()
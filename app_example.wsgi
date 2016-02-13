#! /usr/bin/python
# -*- coding: utf-8 -*-

import os, sys

sys.path.insert(0,"/path/to/app/dir")

PROJECT_DIR = '/path/to/project/dir'


activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
print PROJECT_DIR
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from webSE import app as application

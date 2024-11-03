#!/usr/bin/env python

import os

BACKEND_ENV_NAME = 'OQUPY_BACKEND'
if BACKEND_ENV_NAME in os.environ:
    print(os.environ['OQUPY_BACKEND'])
else:
    print('UNSET')
#for key, value in os.environ.items():
#    print('{}: {}'.format(key, value))

class A:
    HELLO='123'
class test:
    def __init__(self, name=A.HELLO):
        print(name)
t = test()

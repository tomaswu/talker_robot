#-*- coding:utf-8 -*-
'''
    @Author: Tomas
    @Date: 2020-01-16 09:23:36
    @Last Modified by:   Tomas
    @Last Modified time: 2020-01-16 09:23:36
    Desc:
'''

import time

class clock():
    def __init__(self):
        self.judg=True
        self.interval=0.002
    
    def wait(self):
        while self.judg:
            time.sleep(self.interval)
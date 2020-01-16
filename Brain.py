#-*- coding:utf-8 -*-
'''
    @Author: Tomas
    @Date: 2020-01-15 15:53:50
    @Last Modified by:   Tomas
    @Last Modified time: 2020-01-15 15:53:50
    Desc:
'''

import numpy as np
import os,time,sys
import communication
from threading import Thread
import queue
import clock

auto_listen_mode=True
listen=None
talker=None

class brain():
    def __init__(self,word_talker):
        self.thd=Thread(target=self.wake,args=(word_talker,))
        self.thd.daemon=True
        self.thd.start()

    def wake(self,word_talker):
        global listen,talker,auto_listen_mode
        talker,listen = word_talker
        while True:
            if not auto_listen_mode:
                time.sleep(0.002)
                continue
            if not listen.empty():
                word=listen.get()
                answer=communication.word_process(word)
                talker.emit(answer)
            time.sleep(0.001)
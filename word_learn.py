#-*- coding:utf-8 -*-
'''
    @Author: Tomas
    @Date: 2020-01-15 16:13:07
    @Last Modified by:   Tomas
    @Last Modified time: 2020-01-15 16:13:07
    Desc:
'''

import numpy as np
import os,time,sys
import word_consider
import Model
import Brain

imitation_history=[]

def learning(word):
    if word_consider.think_mode==1:
        Brain.auto_listen_mode=False
        while Brain.listen.empty():
            time.sleep(0.002)
        answer=Brain.listen.get()
        Model.normal_word[word]=answer
        Brain.talker.emit(f'我学会怎么回答“{word}”了')
        Brain.auto_listen_mode=True
        word_consider.think_mode=1
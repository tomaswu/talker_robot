# -*- coding:utf-8 -*-
'''
    @Author: Tomas
    @Date: 2020-01-15 16:51:16
    @Last Modified by:   Tomas
    @Last Modified time: 2020-01-15 16:51:16
    Desc:
'''

import numpy as np
import os
import sys
import time
import Model
import word_learn
from threading import Thread

# that think mode include 3 mode
# 0 means answer directly
# 1 means simple imitation
think_mode = 0


def think(word):
    global think_mode
    if think_mode == 0:
        try:
            answer = Model.model['word_think'].process(word)
        except:
            think_mode = 1
            answer = think(word)
    elif think_mode == 1:
        notice(word)
        answer = f'请告诉我该怎么回答：\"{word}\"'
    return answer

def notice(word):
    thd=Thread(target=word_learn.learning,args=(word,))
    thd.daemon=True
    thd.start()
    


# test
if __name__=="__main__":
    print(think('hello'))
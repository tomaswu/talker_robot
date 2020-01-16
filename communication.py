#-*- coding:utf-8 -*-
'''
    @Author: Tomas
    @Date: 2020-01-15 16:16:06
    @Last Modified by:   Tomas
    @Last Modified time: 2020-01-15 16:16:06
    Desc:
'''

import numpy as np
import Model
import word_consider

def word_process(question):
    if question in Model.model['normal'].keys():
        answer=Model.model['normal'][question]
    else:
        answer=word_consider.think(question)
    return answer
#-*- coding:utf-8 -*-
'''
    @Author: Tomas
    @Date: 2020-01-15 16:16:42
    @Last Modified by:   Tomas
    @Last Modified time: 2020-01-15 16:16:42
    Desc:
'''

import pickle,os

normal_word={'你是谁':'我是罗伯特'}
word_symbol=[]
model={'normal':normal_word,'word_symbol':word_symbol}


if os.path.isfile('memory.pkl'):
    with open('./memory.pkl','rb') as f:
        normal_word,model=pickle.load(f)
        word_symbol=model['word_symbol']

def model_save():
    global normal_word, model
    with open('memory.pkl','wb') as f:
        pickle.dump([normal_word,model],f)

if __name__=="__main__":
    model_save()
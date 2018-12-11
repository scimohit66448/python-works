# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 12:12:47 2018

@author: mohit
"""

def mf(*b):
    print(b)
mf(1,2,3,4,5,6,7)
def sample_functions():
    print("this is functions example")
sample_functions()
def specific_functions(name='not entered',age='not entered',address='not given'):
    print(name,age,address,sep="\n")
specific_functions()
specific_functions('john',21,'allahabad')
# -*- coding: utf-8 -*-
import os
from flsystem import *

def cd_now():
    tmp = os.getcwd()
    return os.path.split(tmp)[-1]
    
def cd_up():
    tmp = os.getcwd()
    tmp = os.path.split(tmp)[0]
    os.chdir(tmp)
    return os.path.split(tmp)[-1]

def cd_down(dirname):
    os.chdir(dirname)
    return dirname

commands = globals()

while True:
    com = raw_input('> ')
    tmp = com.split(' ')
    command = tmp.pop(0) + '_' + tmp.pop(0)
    result = commands[command](*tmp)
    if result != None:
        print result
    
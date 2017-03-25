# -*- coding: utf-8 -*-
import os
import shutil

# manipulate file
def create_file(filename):
    """create a file"""
    with open(filename, 'w') as f:
        pass

def delete_file(filename):
    """delete a file"""
    os.remove(filename)

def open_file(filename):
    """open a file"""
    result = ''
    with open(filename) as f:
        result = f.read()
    return result
    
def list_file():
    """list all file"""
    return [x for x in os.listdir('.') if os.path.isfile(x)]

def is_file(filename):
    """whether is file"""
    return os.path.isfile(filename)
    
# manipulate directionary
def create_dir(dirname):
    """create a directionary"""
    os.mkdir(dirname)
      
def delete_dir(dirname):
    """delete a directionary"""
    os.rmdir(dirname)
    
def open_dir(filename):
    """open a directionary"""
    return os.listdir(filename)

def list_dir():
    """list all directionary"""
    return [x for x in os.listdir('.') if os.path.isdir(x)]

def is_dir(dirname):
    """whether is directionary"""
    return os.path.isdir(dirname)

# manipulate mixture
def move_any(name, dirname):
    """"move any"""
    shutil.move(name, dirname)
    
def rename_any(oldname, newname):
    """rename any"""
    os.rename(oldname, newname)
    
def find_all(name):
    """find all"""
    results = []
    tmp = os.listdir('.')
    
    while tmp:
        t = tmp.pop(0)
        if os.path.isdir(t):
            s = os.listdir(t)
            for x in s:
                y = os.path.join(t, x)
                if x == name:
                    results.append(y)
                tmp.append(y)
                
    return results

def list_all():
    """list all"""
    return os.listdir('.')

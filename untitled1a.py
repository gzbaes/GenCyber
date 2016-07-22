# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 10:05:36 2016

@author: student
"""

import hashlib
def md5(fname): 
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f: 
        for chunk in iter(lambda: f.read(4096),b""): 
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

print(md5("Copy of facebook_is_lame.jpg"))
print(md5("Copy of wishing_to_shave.jpg"))
    

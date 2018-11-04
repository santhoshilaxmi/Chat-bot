# -*- coding: utf-8 -*-
"""
Created on Sat Sep 08 10:28:28 2018

@author: DELL
"""
import re
list_noise=['an','the','santa']

def remove_noise(input_data):
    words=input_data.split()
    free_noise=[]
    free_noise=[word for word in words if word not in list_noise]
    free_text=" ".join(free_noise)
    print(free_text)
remove_noise("santhoshi is AN the santa santathe")
i="santhu santhi santa"
print(i.group().strip())

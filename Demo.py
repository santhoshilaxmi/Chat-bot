# -*- coding: utf-8 -*-
"""
Created on Sat Sep 08 12:10:53 2018

@author: DELL
"""
import re
import itertools

"""girl_1=re.finditer(r".", "abc")
'print(girl_1.group().strip())"""

print(list(itertools.combinations(['1','2','3'],2)))

print(list(itertools.combinations_with_replacement(['1','2','3'],2)))

print(list(itertools.permutations(['1','2','3'],2)))

print(list(itertools.product(['1','2','3'])))

list5 = .join(" g",itertools.combinations(['1','2','3'],2))



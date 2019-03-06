# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:00:57 2019
CyclicRotation
@author: cyborg001
"""
v = [n for n in range(1,10)]

def solution(v,r):
    length = len(v)
    vtemp = length*[0]
    for i in range(length):
        posi = (i+r)%length
        print(i+1,posi)
        vtemp[posi]=v[i]
    return vtemp

print(solution(v,3))
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 07:12:23 2019

@author: cyborg001
"""

def solution(A):
    f = dict()
    for n in A:
        if n in f:
            f[n]+=1
        else:
            f[n]=1
    #print(f)
    for n in f:
        if f[n]%2 != 0:
            return n
A = [9, 3, 9, 3, 9, 7,9]
print(solution(A))

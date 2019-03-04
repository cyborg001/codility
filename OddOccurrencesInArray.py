# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 07:12:23 2019

@author: cyborg001
"""

def solution(A):
    while True:
        e = A.pop()
        if e in A:
            A.remove(e)
        else:
            return e
        print(A)
            #return e
A = [9, 3, 9, 3, 9, 7, 9]
print(solution(A))

# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:44:35 2019

***PermCheck: programa que chequea si un conjunto
***de numeros es una permutacion

@author: cyborg001
"""

def solution(A):
   
        
    if len(A)==0:
        return 0
    if len(A)==1:
        if A[0]==1:
            return 1
        return 0
    k = max(A)
    if k-1 != len(A) or A != list(set(A)) :
        return 0
    
    ser2 = int((k)*(k+1)/2)
    tot = sum(A)
    
    if tot == ser2:
        return 1
    else:
        return 0


A = []

def serie(k,i):
    return int((k-i)*(k+i+1)/2)
print(solution(A))
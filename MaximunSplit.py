# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 07:26:07 2019
Programa que divide un vector en dos regiones
a partir de un numero P dado. buscar cual es el
 numero P que da la mayor diferencia entre ambos bloques
@author: cyborg001

"""

def solution(A):
    smaller = max(A)
    for p in A:
        diff = abs(sum(A[:p])-sum(A[p:])) 
        if diff < smaller:
            smaller = diff
    return smaller
A=[3,1,2,4,3]
print(solution(A))
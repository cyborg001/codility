# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 07:26:07 2019
Programa que divide un vector en dos regiones
a partir de un numero P dado. buscar cual es el
 numero P que da la mayor diferencia entre ambos bloques
@author: cyborg001

"""

def solution(A):
    total = sum(A)
    left = 0
    right = 0
    mini = None
    for i in range(len(A)-1):
            left += A[i]
            right = total - left
            dif = abs(left - right) 
            print (left,right,dif)
            if mini == None:
                mini = dif
            else:
                if mini > dif:
                    mini = dif
    return mini
A=[-3000,-1000]
print(solution(A))
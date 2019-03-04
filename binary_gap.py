# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 01:29:54 2019

@author: el_in
"""

#binary gap
def solution(N):
    v=[]
    while N > 1:
        v.append(N%2)
        N//=2
    v.append(N%2) 
    v = v[-1::-1]
    #indexes = []
    #print(v)
    first = True
    maxi =0
    #cont = 0
    t=0
    for i in range(len(v)):
        if first and v[i] == 1:
           #cont+=1
           t=i
           #indexes.append(i)
           first = False
        elif v[i] == 1:
            if v[i-1]==1:
                t = i
            else:
                if i - t -1 > maxi:
                    maxi = i-t-1
                t=i
            #cont+=1
                #indexes.append(i)
    #print(indexes)   
    return maxi
print(solution(561892))
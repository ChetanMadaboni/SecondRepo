# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:37:18 2020

@author: HP
"""
def add(a,b):
    return a+b
if __name__=='__main__':
    n=int(input())
    for _ in range(n):
        ab=list(map(int,input().strip().split()))
        print(add(ab[0],ab[1]))
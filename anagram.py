# -*- coding: utf-8 -*-
"""
Created on Sat May 30 08:36:25 2020

@author: HP
"""

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        st=input().strip()
        wrd=st.split(" ")
        s1=0
        s2=0
        for i in  wrd[0]:
            s1=s1+ord(i)
        for i in wrd[1]:
            s2=s2+ord(i)
        if(s1==s2):
            print(True)
        else:
            print(False)
            
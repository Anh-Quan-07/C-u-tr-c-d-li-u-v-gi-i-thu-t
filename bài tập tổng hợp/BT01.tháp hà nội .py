# -*- coding: utf-8 -*-
"""
Created on Tue May  4 10:11:08 2021

@author: quann
"""

def thapHaNoi(n, toaMot, toaHai, toaBa):

    if n == 1:
        print("Chuyen tu", toaMot, "sang", toaBa)
    else:
        thapHaNoi(n-1,toaMot,toaBa ,toaHai)
        print("Chuyen tu", toaMot, "sang", toaBa)
        thapHaNoi(n-1,toaHai,toaMot, toaBa)

def ucln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)
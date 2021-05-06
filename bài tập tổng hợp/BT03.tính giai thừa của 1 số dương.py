# -*- coding: utf-8 -*-
"""
Created on Tue May  4 10:09:31 2021

@author: quann
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Nhập một số để tính giai thừa : "))
print(factorial(n))
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 21:23:32 2021

@author: quann
"""

def uscln(a, b):
    if a < 0 or b < 0:
        return None
    if b == 0:
        return a
    return uscln(b, a % b)

a = int(input("Nhập số nguyên dương a = "))
b = int(input("Nhập số nguyên dương b = "))
print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b))
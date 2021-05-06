# -*- coding: utf-8 -*-
"""
Created on Tue May  4 10:14:10 2021

@author: quann
"""

"""
 * Tìm ước số chung lớn nhất (USCLN)
 *
 * @param a: số nguyên dương
 * @param b: số nguyên dương
 * @return USCLN của a và b
"""
def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b)
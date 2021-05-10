# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:13:32 2021

@author: quann
"""

quick_sort<-function(x)
{
  if(length(x)<=1) return(x)
  pivot<-x[1]
  rest<-x[-1]
  pivot_less<-quick_sort(rest[rest<pivot])
  pivot_greater<-quick_sort(rest[rest>=pivot])
  return(c(pivot_less,pivot,pivot_greater))
}
dulieu = c(32, 17, 49, 98, 06, 25, 53, 61)
quick_sort(dulieu)
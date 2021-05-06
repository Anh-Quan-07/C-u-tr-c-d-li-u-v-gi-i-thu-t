# -*- coding: utf-8 -*-
"""
Created on Tue May  4 10:32:18 2021

@author: quann
"""

class Queue:

  def __init__(self):
      self.queue = list()

  def addtoq(self,dataval):
# Chen phuong thuc de them phan tu
      if dataval not in self.queue:
          self.queue.insert(0,dataval)
          return True
      return False

  def size(self):
      return len(self.queue)

TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.size())
# -*- coding: utf-8 -*-
"""factwithctrl

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pHKoA-9YPjn6f0qHYrquPvlOKwQJqlcM
"""

n=int(input())
fact=1
i=1
while n<=20:
  while i<=n:
    fact=fact*i
    i+=1
  break
print(fact)
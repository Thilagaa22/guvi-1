# -*- coding: utf-8 -*-
"""factorial

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n7ocHd2eDpDhX6-pJjjQrNlQhad1AaAF
"""

n=int(input())
factorial=1
if n==0:
   print("1")
else:
   for i in range(1,n+1):
       factorial = factorial*i
   print(factorial)

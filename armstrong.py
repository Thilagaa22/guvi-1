# -*- coding: utf-8 -*-
"""armstrong

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W8nT7msgDBWxERUzF3TnSyNHgfWcuTPM
"""

n=int(input())
order=len(str(n))
temp=n
sum=0
while temp>0:
  digit=temp%10
  sum+=digit**order
  temp//=10
if n==sum:
  print("yes")
else:
  print("no")

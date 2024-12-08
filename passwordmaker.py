#!/usr/bin/python3
import random
import string
 
n=5
passWord = ''
ab = list(string.ascii_letters)

for i in range(0,10):
    ab.append(i)
  
for _ in range(n):
    x = random.randint(0,len(ab)-1)
    y = str(ab[x])
    passWord=passWord+y
 
print(passWord)
# -*- coding: utf-8 -*-
"""
tac gia: Le Duc Trong
ngay: 14/12/2019
mo ta: Cu phap can ban
"""
#String

s = 'le duc trong'
print (s[0:2])

a = 'Le'
b = 'Duc'
c = 'Trong'
e = ' '
name = a+e+b+e+c
print (name)

d = len(name)
print (d)

#Number

n1 = 2
n2 = 5
n3 = n1 * n2
print (n3)

n3 = n1 ** n2
print (n3)

n3 = n1 / n2
print (n3)

n4 = 'a       g'
print (n3)

#Errol
#Print-abcd
#"abc"/5

#List

list = [1,2,3,4,5,6]
print (list[0:2])

list1 = [a,b,c]
list2 = [list,list1]

print(list2[0][2])
print(list2[1][0:1])

#n = len(list1)
#i=0
#while i < n:
 #   print(list1[i], end=', ')
  #  i=i+1
    

n = len(list2[1])
i=0
while i < n:
    print(list2[1][i], end=', ')
    i=i+1

#More Control Flow Tools
#If-Else
x = int(input("Please enter an integer: "))
#Input-Nhap
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
    

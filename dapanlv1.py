# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 08:14:49 2019

@author: User
"""

#Bài tập python lv1
#Bài 1
i = []
for a in range (2000, 3201):
    if ( a % 7 == 0 ) :
        if ( a % 5 != 0) :
            i.append(str(a))
print (','.join(i)) #In một dãy phần tử ngăn cách bởi dấu phẩy
                    # Ex: 2,1,4,6,7

#Bài 2

a = int(input('Enter Number:'))    
gt = 1
for i in range(1, a+1) :
    gt = gt*i
print (gt)
    
#Bài 3
n=int(input("Enter Number:"))
d=dict() #Dictionary
for i in range(1,n+1):
    d[i]=i*i

print (d)
#Bài 4
a= input('Enter Number: ')
l=a.split(",") #???
t=tuple(l) #???
print ( l )
print ( t )

#Bài 5
name = str(input('Enter name: '))
print ( name.upper() ) #Đổi chữ thường sang chữ hoa

#Bài 6
a = int(input('Enter number: '))
print( a*a )


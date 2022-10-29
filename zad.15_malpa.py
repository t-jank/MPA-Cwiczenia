# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 01:18:00 2022

@author: t-jan
"""

'''
Zadanie 15. Małpa pisze na klawiaturze mającej 26 małych liter (alfabet ang-
ielski). Każda litera może wystąpić niezależnie od innych z tym samym praw-
dopodobieństwem. Jeśli małpa napisała 1000000 liter, jaka jest wartość oczeki-
wana liczby wystąpień słowa "dowod"?
'''


import random

alfabet=('q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m')

repeat_number = 500
number_of_letters = 1000000
suma = 0


for rn in range(0,repeat_number):

    rand_letters = random.choices(alfabet, k = number_of_letters)
    napis=''
    for i in range(0,number_of_letters): # string z tablicy liter
        napis = napis + rand_letters[i]
     
    res = [i for i in range(len(napis)) if napis.startswith('dowod', i)]
  
    if len(res)>1:
        print('O!',len(res))
        
    suma += len(res)

print("Średnia liczba wystąpień słowa 'dowod' w",number_of_letters,"liter:", suma/repeat_number)

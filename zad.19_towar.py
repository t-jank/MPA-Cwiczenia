# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 14:14:40 2022

@author: t-jan
"""

'''
Zadanie 19. Załóżmy, że każdego dnia towar o cenie q podrożeje r razy z
prawdopodobieństwem p lub stanieje do ceny q/r z prawdopodobieństwem 1−p.
Cena początkowa towaru to 1 zł. Oblicz wartość oczekiwaną i wariancję ceny
towaru po d dniach.
'''


import random

start_price = 1
r = 10
p = 0.56
d = 10 # liczba dni

for i in range(0,d):
    a=0
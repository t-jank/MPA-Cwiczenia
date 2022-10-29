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

q = 256 # price
r = 2
p = 0.5
d = 100 # liczba dni

for i in range(0,d):
    x = random.random()
    if x < p:
        q = q * r
    else:
        q = q / r

print('Cena towaru po', d, 'dniach:', q)

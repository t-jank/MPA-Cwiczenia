# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 15:19:29 2022

@author: t-jan
"""

'''
Zadanie 20. Rzucamy symetryczną monetą 100 razy. Oblicz prawdopodobieństwo
wypadnięcia 55 lub więcej orłów. Porównaj obliczone prawdopodobieństwo z
ograniczeniem otrzymanym z nierówności Chernoffa. Wykonaj podobne obliczenia
dla 1000 rzutów monetą i prawdopodobieństwa wypadniecie co najmniej 550
orłów.
'''
'''
Analitycznie:
Nierównosć Chernoffa: P( X >= (1+delta)*EX ) <= [(e^delta) / (1+delta)^(1+delta)]^EX
EX=50(500) -> delta=0.1 -> P(X>=50,n=100)<=0.79; P(X>=500,n=1000)<=0.089
# Wyniki:
# P(X>=55,n=100) = 0.1841008086633481  # dokladny wynik
# P(X>=50,n=100) <= 0.7850091625435333  # Chernoff
# P(X>=550,n=1000) = 0.0008652680424881586  # dokladny wynik
# P(X>=500,n=1000) <= 0.08886837892405824  # Chernoff
'''
import math
import random

def NewtonSymbol(n,k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

n = 1000 # liczba prob
k = 550 # liczba sukcesow
p = 1/2 # prawdopodobienstwo sukcesu
# Liczymy P( X >= k )

################ CHERNOFF #################
pchernoff = (math.exp(0.1) / 1.1**1.1)**(n*p) # bedzie sie psuc po zmianie p, bo inna delta
print('Z nierownosci Chernoffa:\n',' P(X >=',k,', n=',n,') <= ',pchernoff, sep='')

############## ANALITYCZNIE ###############
prawdop = 0
for i in range(k,n+1):
    prawdop += NewtonSymbol(n,i)*p**i*(1-p)**(n-i)
print('Analitycznie:\n',' P(X >= ',k,', n=',n,'): ',prawdop, sep='')

############## SYMULACJA ##################
repeat_number = 10000
sum = 0
for rn in range(0,repeat_number):
    lsukcesow = 0
    for i in range(0,n):
        x = random.random()
        if x >= p:
            lsukcesow+=1
    if lsukcesow >= k:
        sum+=1
print('Symulacyjnie:\n',' P(X >= ',k,', n=',n,'): ',sum/repeat_number, sep='')


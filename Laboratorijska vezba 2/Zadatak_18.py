"""Korišdenjem programskog jezika Python, napisati funkciju brojevi, koja iz stringa izvlači listu svih 
brojeva koji se u njemu nalaze. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi). 
Primer: brojevi("42+10=52;10*10=100") = [ 42, 10, 52, 10, 10, 100 ] """

from re import *

def brojevi(text):
    return list(map(lambda x: int(x), findall(r'(\d+)', text)))

print(brojevi("42+10=52;10*10=100"))
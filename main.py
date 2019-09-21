#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sencill programa de xifrat i desxifrat per substitució (tipus xifrat cèsar)
# alfabet text en clar: lletres alfabet anglès 'a'..'z' (només minúscules) + signes de puntuació (no s'encripten)
# alfabet text xifrat : el mateix

L = 26 # nombre caràcters alfabet

def obteNum(text):
# retorna un enter corresponent al desplaçament d'un simple xifrat tipus Cèsar
    desp = input(text)
    return int(desp) 
    
def codifica(caracter, despl):
# si caràcter és lletra 'a'..'z' retorna <caracter> codificat usant <despl>
# altrament retorna caràcter tal qual
    if caracter >= 'a' and caracter <='z':
        return chr(((ord(caracter) - ord('a') + despl) % L) + ord('a'))
    else:
        return caracter
        
def descodifica(caracter, despl):
# si caràcter és lletra 'a'..'z' retorna <caracter> codificat usant <despl>
# altrament retorna caràcter tal qual
    if caracter >= 'a' and caracter <='z':
        return chr(((ord(caracter) - ord('a') - despl) % L) + ord('a'))
    else:
        return caracter
        
def cesar():
# obté un desplaçament i un text, i mostra el text codificat amb mètode Cèsar (amb el desp. entrat)
# després el decodifica i mostra l'original
    desp = obteNum("entreu un nombre natural corresponent al desplaçament: ")
    text = input("entra el text que vols xifrar: ")
    text_xifrat = ""
    for k in range(len(text)):
        text_xifrat += codifica(text[k], desp)
    print("TEXT XIFRAT: ", text_xifrat) 
    # ara decodificarem
    text_original = ""
    for k in range(len(text_xifrat)):
        text_original += descodifica(text[k], desp)
    print("TEXT ORIGINAL: ", text_original) 
        

class PolyTuple:
    def __init__(self, letter, row, column):
        self.letter = letter
        self.row = row
        self.column = column

def polybios():
    print("Entreu el nombre de files i columnes, recorda dimensionar correctament la matriu!")
    f = obteNum("Entra el nombre de files : ")
    c = obteNum("Entra el nombre de columnes : ")

    # Representem la matriu com un vector lineal on hi ha tants elements com lletres de l'alfabet. 
    vector = [0 for x in range(L)]

    # Per representar la matriu es crea un objecte PolyTuple que conté els valors per la lletra, la fila i la columna de la matriu. 
    # FORMAT DEL VECTOR :  
    # lletra  : | a | b | c | ...
    # fila    : | A | A | A | ...
    # columna : | A | B | C | ...

    # Es monta així per tres raons : 
    # - Simplicitat, és més senzill de tractar les colisions fruit del tamany de la matriu al construïr-la
    # - Claretat del codi, amb un while es pot muntar la matriu sencera
    # - Ordre de complexitat, les cerques sempre son O(n) on n pot pendre com màxim el nombre de lletres de l'alfabet - 1.
    # Si considerem cerques no lineals es pot cercar en complexitat logaritmica. 
    letter = 'a'
    row = 'A'
    col = 'A'
    while(ord(letter) < L + ord('a')):
        vector[ord(letter) - ord('a')] = PolyTuple(letter, row, col)
        letter = chr(ord(letter) + 1)
        

    print(vector)

polybios()
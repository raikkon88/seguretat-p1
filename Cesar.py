#!/usr/bin/env python
# -*- coding: utf-8 -*-
# senzill programa de xifrat i desxifrat per substitució (tipus xifrat cèsar)
# alfabet text en clar: lletres alfabet anglès 'a'..'z' (només minúscules) + signes de puntuació (no s'encripten)
# alfabet text xifrat : el mateix

import Utils

L = 26 # nombre caràcters alfabet
    
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
        
def codificaText(text, desp):
    text_xifrat = ""
    for k in range(len(text)):
        text_xifrat += codifica(text[k], desp)
    return text_xifrat

def descodificaText(text, desp):
    text_original = ""
    for k in range(len(text)):
        text_original += descodifica(text[k], desp)
    return text_original

def cesar():
# obté un desplaçament i un text, i mostra el text codificat amb mètode Cèsar (amb el desp. entrat)
# després el decodifica i mostra l'original
    desp = Utils.obteNum("Entreu un nombre natural corresponent al desplacament: ") % L
    text = input("entra el text que vols xifrar: ")
    text_xifrat = codificaText(text, desp)
    print("TEXT XIFRAT: ", text_xifrat)
    # ara decodificarem
    print("TEXT ORIGINAL: ", descodificaText(text_xifrat, desp))

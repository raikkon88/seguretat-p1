#!/usr/bin/env python
# -*- coding: utf-8 -*-
# senzill programa de xifrat i desxifrat per transformació (tipus xifrat Rail fence)
# alfabet text en clar: lletres alfabet anglès 'a'..'z' (només minúscules) + signes de puntuació (Sí que es processen)
# alfabet text xifrat : el mateix (amb signes de puntuació).

import Utils

L = 26 # nombre caràcters alfabet

def codifica(text, rails):
# Retorna el text codificat en railfence amb rails.
# Codifica tots els caràcters ja que és per transformació i no per substitució.

    # S'ha de muntar el sistema de rails. 
    vector = [list() for x in range(rails)]
    k = 0
    while k < len(text):
        vector[k % rails].append(text[k])   
        k += 1

    text_xifrat = ""
    for v in vector:
        for l in v:
            text_xifrat += l


    return text_xifrat
        
def descodifica(text, rails):
# Descodifica un text codificat en railfence amb el nombre de rails
    filesMajors = (len(text)) % rails
    carXFila = len(text) // rails

    # S'ha de muntar el sistema de rails. 
    vector = [list() for x in range(rails)]
    
    k = 0
    fila = 0
    while fila < rails:
        c = 0
        while c < carXFila: 
            vector[fila].append(text[k])
            c += 1
            k += 1
        
        if fila < filesMajors: 
            vector[fila].append(text[k])
            k += 1

        fila += 1

    text_desencriptat = ""

    k = 0
    while k < len(text):
        text_desencriptat += vector[k % rails][k // rails]
        k += 1

    return text_desencriptat


def railFence():
# obté un valor per els rails i un text, i mostra el text codificat amb mètode Rail Fence (amb el nombre de rails entrat)
# després el decodifica i mostra l'original
    rails = Utils.obteNum("entreu un nombre natural corresponent al Nombre de rails: ")
    text = input("entra el text que vols xifrar: ")
    text_xifrat = codifica(text, rails)
    print("TEXT XIFRAT:", text_xifrat) 
    text_original = descodifica(text_xifrat, rails)
    print("TEXT ORIGINAL:", text_original) 

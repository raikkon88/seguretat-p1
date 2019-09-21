#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programa per la pràctica 1 de seguretat i protecció de dades. 
# Permet executar els algoritmes cesar, polibios i railfence. 

import PolyBios
import Cesar
import RailFence

def main(): 
# Codifica un text entrat per teclat. 
# Si el text entrat per teclat és buit codifica el text de l'enunciat de la pràctica
# La codificació és amb els mètodes : Cesar, PolyBios i RailFence. 
# En el cas de RailFence també desordena els espais ja que és un mètode de transformació i ho pot fer.

    print("Entra el text que vols codificar i descodificar,")
    print("Si apretes INTRO fara automaticament el de l'apartat d. ")
    text = input("text : ")
    if text == "": 
        text = "it's the honky tonk women that gimme, gimme, gimme the honky tonk blues (honky tonk women, by the rolling stones)"

    cesar = Cesar.codificaText(text, 17)
    print("Amb el metode Cesar : ")
    print(cesar)

    print()
    print("------------------------------------")

    print("Amb el metode PolyBios : ")
    polybios = PolyBios.codificaText(text, 5, 5)
    print(polybios)

    print()
    print("------------------------------------")

    # En aquest cas el text no concordarà del tot àmb una possible solució teva ja que també es codifiquen TOTS els caràcters!! 
    print("Amb el metode RailFence : ")
    railFence = RailFence.codifica(text, 7)
    print(railFence)

    print()
    print("------------------------------------")

main()
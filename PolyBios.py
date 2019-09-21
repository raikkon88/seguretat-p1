#!/usr/bin/env python
# -*- coding: utf-8 -*-
# senzill programa de xifrat i desxifrat per substitució (tipus xifrat PolyBios)
# alfabet text en clar: lletres alfabet anglès 'a'..'z' (només minúscules) + signes de puntuació (no s'encripten)
# alfabet text xifrat : el mateix

L = 26 # nombre caràcters alfabet

import Utils

## CLASS DEFINITION 
##########################################################################

# Tupla creada per poder agrupar els valors de les lletres amb els valors de la fila i la columna de la taula.
class PolyTuple:
    def __init__(self, letter, row, column):
        self.letter = letter
        self.row = row
        self.column = column

    def __str__(self):
        return "[" + self.letter + "," + self.row + "," + self.column + "]"

    def __repr__(self):
        return str(self)

def codifica(caracter, vector):
# si caràcter és lletra 'a'..'z' retorna <caracter> codificat usant la combinació de <vector>
# altrament retorna caràcter tal qual
    if caracter >= 'a' and caracter <='z':
        for t in vector:
            if t.letter == caracter: 
              return t.row + t.column
    else:
        return caracter
        
def descodifica(fila, columna, vector, files, columnes):
# si caràcter és lletra 'a'..'z' retorna <caracter> descodificat usant la combinació de <vector>
# altrament retorna caràcter tal qual
    if fila >= 'A' and fila <= chr(ord('A') + files) and columna >= 'A' and columna <= chr(ord('A') + columnes):
        k = 0
        while k < len(vector) and not (vector[k].row == fila and vector[k].column == columna): 
            k += 1
        ## Si no l'he trobat
        if k == len(vector):
            return fila + columna
        
        # Si l'he trobat
        return vector[k].letter

    else:
        return fila+columna

def createMatrix(f, c):
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
        # Per adaptar-nos a la taula de les transparències es fa colisionar la i i la j. 
        if(letter == 'j' and f == 5 and c == 5):
            vector[ord(letter) - ord('a')] = PolyTuple(letter, 'B', 'D')
            letter = chr(ord(letter) + 1)
        else:
            vector[ord(letter) - ord('a')] = PolyTuple(letter, row, col)
            letter = chr(ord(letter) + 1)
            col = chr(ord(col) + 1)
            
            if (ord(col) - ord('A')) % c == 0: 
                col = 'A'
                row = chr(ord(row) + 1)
                if (ord(row) - ord('A')) % f == 0: 
                    row = 'A'

    return vector

def codificaText(text, f, c):

    # Codifiquem
    text_xifrat = ""
    vector = createMatrix(f, c)
    
    for k in range(len(text)):
        text_xifrat += codifica(text[k], vector)

    return text_xifrat

def descodificaText(text_xifrat, f, c):
    # ara decodificarem
    text_original = ""
    vector = createMatrix(f, c)

    k = 0
    while(k + 1 < len(text_xifrat)):
        if text_xifrat[k] >= 'A' and text_xifrat[k] <= 'Z':
            text_original += descodifica(text_xifrat[k], text_xifrat[k+1], vector, f, c)
            k +=2
        else: 
            text_original += text_xifrat[k]
            k += 1

    return text_original

def polybios():
# Obté el nombre de files i de columnes i un text i mostra el text codificat en polybios
# Després mostra el text descodificat

    print("Entreu el nombre de files i columnes, recorda dimensionar correctament la matriu => files >= 5 and columnes >= 5!")
    f = Utils.obteNum("Entra el nombre de files : ")
    c = Utils.obteNum("Entra el nombre de columnes : ")
    if f < 5 or c < 5: 
        print("nombre de files < 5 o nombre de columnes < 5")
        polybios()
    else:
      text = input("entra el text que vols xifrar: ")
      text_xifrat = codificaText(text.lower(), f, c)
      print("TEXT XIFRAT: ", text_xifrat) 
      text_original = descodificaText(text_xifrat, f, c)
      print("TEXT ORIGINAL: ", text_original) 

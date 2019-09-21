
import os
os.environ["PYTHONIOENCODING"] = "utf-8"
# sencill programa de xifrat i desxifrat per substitució (tipus xifrat PolyBios)
# alfabet text en clar: lletres alfabet anglès 'a'..'z' (només minúscules) + signes de puntuació (no s'encripten)
# alfabet text xifrat : el mateix

L = 26 # nombre caràcters alfabet




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


def obteNum(text):
# retorna un enter corresponent al desplaçament d'un simple xifrat tipus Cèsar
    desp = input(text)
    return int(desp) 

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
        found = False
        k = 0
        char = ""
        while k < len(vector) and not (vector[k].row == fila and vector[k].column == columna): 
            k += 1
        ## Si no l'he trobat
        if k == len(vector):
            return fila + columna
        
        # Si l'he trobat
        return vector[k].letter

    else:
        return fila+columna

def polybios():
    print("Entreu el nombre de files i columnes, recorda dimensionar correctament la matriu!")
    f = obteNum("Entra el nombre de files : ")
    c = obteNum("Entra el nombre de columnes : ")

    print(f)
    print(c)
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
        col = chr(ord(col) + 1)
        
        if (ord(col) - ord('A')) % c == 0: 
            col = 'A'
            row = chr(ord(row) + 1)
            if (ord(row) - ord('A')) % f == 0: 
                row = 'A'

    print(vector)

    # Codifiquem
    text_xifrat = ""
    text = input("entra el text que vols xifrar: ")
    for k in range(len(text)):
        text_xifrat += codifica(text[k], vector)

    print("TEXT XIFRAT: ", text_xifrat) 

    # ara decodificarem
    text_original = ""

    k = 0
    while(k + 1 < len(text_xifrat)):
        if text_xifrat[k] >= 'A' and text_xifrat[k] <= 'Z':
            text_original += descodifica(text_xifrat[k], text_xifrat[k+1], vector, f, c)
            k +=2
        else: 
            text_original += text_xifrat[k]
            k += 1
          

    print("TEXT ORIGINAL: ", text_original) 


polybios()
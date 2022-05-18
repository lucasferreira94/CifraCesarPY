from random import randint
from string import ascii_lowercase as lc

# key = randint(1, 25)
key = 5

def encryption():
    indice = 0
    resultado = ''
    file = open('plaintext.txt', 'a+')
    for linha in file:
        for letra in linha:  # ITERANDO SOBRE CADA CARACTERE DO TEXTO
            if letra in lc:
                index = lc.find(letra)  # ENCONTRA O INDICE EXATO DO CARACTERE
                index = (index + key) % 26
                resultado += lc[index]
    return resultado

while True:
    mode = str(input('Qual será o modo? [enc] ou [dec]: '))
    if mode == 'enc':
        operacao = encryption()
        break
    else:
        break



from random import randint
from string import ascii_lowercase as lc

# key = randint(1, 25)
key = 5

def encryption():
    indice = 0
    resultado = ''
    file = open('plaintext.txt', 'r')
    for linha in file:
        for letra in linha:                           # ITERANDO SOBRE CADA CARACTERE DO TEXTO
            if letra in lc:
                index = lc.find(letra)                # ENCONTRA O INDICE EXATO DO CARACTERE
                index = (index + key) % 26            # CÁLCULO PARA REALIZAR A CIFRA DO CARACTERE
                resultado += lc[index]                # CONCATENA O RESULTADO COM OS ANTERIORES
                file_2 = open('ciphertext.txt', 'w+')
                file_2.write(resultado)

def decrypt():
    indice = 0
    resultado = ''
    file = open('ciphertext.txt', 'r')
    for linha in file:
        for letra in linha:
            if letra in lc:
                index = lc.find(letra)
                index = (index - key) % 26
                resultado += lc[index]
                file_2 = open('plaintext.txt', 'w+')
                file_2.write(resultado)
    return print(file_2.read())

while True:
    mode = str(input('Qual será o modo? [enc] ou [dec]: '))
    if mode == 'enc':
        operacao = encryption()
        break
    else:
        break



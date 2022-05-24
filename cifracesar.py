from random import randint
from string import ascii_lowercase as lc

key = randint(1, 26)                                 # VALOR DA CHAVE QUE SERÁ USADO PARA ENCRIPTAR E DECIFRAR

def encryption():
    indice = 0
    resultado = ''
    file = open('plaintext.txt', 'r')
    for linha in file:
        for letra in linha:                           # ITERANDO SOBRE CADA CARACTERE DO TEXTO
            if letra in lc:                           # LETRA ESTA PRESENTE NOS CARACTERES MINUSCULOS IMPORTADOS?
                index = lc.find(letra)                # ENCONTRA O INDICE(POSICAO) EXATO DO CARACTERE
                index = (index + key) % 26            # CÁLCULO PARA REALIZAR A CIFRA DO CARACTERE (ROTACIONAR)
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
                index = (index - key) % 26            # CÁLCULO PARA DECIFRAR CADA CARACTERE (FAZER O REVERSO)
                resultado += lc[index]
                file_2 = open('plaintext.txt', 'w+')
                file_2.write(resultado)

while True:
    mode = str(input('Qual será o modo? [ENC/enc] ou [DEC/dec]: '))
    if mode == 'enc' or mode == 'ENC':
        operacao = encryption()
        break
    elif mode == 'dec' or mode == 'DEC':
        operacao = decrypt()
        break
    else:
        print('modo inválido, digite: "ENC" ou "enc" para encriptar e "DEC" ou "dec" para decriptar', '\n')
        continue



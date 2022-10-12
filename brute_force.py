import importlib
from string import ascii_lowercase as lc
import sys

file = open(sys.argv[1], 'r').read().lower()

def brute_force():
    for key in range(1,26):
        resultado = ''
        print(f'Key: {key}')
        for letra in file:
            if letra in lc:
                index = lc.find(letra)
                index = (index - key) % 26
                resultado += lc[index]
        else:
            resultado += letra
    
        print(resultado)

if __name__ == '__main__':
    brute_force()

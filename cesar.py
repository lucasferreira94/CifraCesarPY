import sys
from string import ascii_lowercase as lc

def help():
    print('Modo de uso: \n'
      'python3 cesar.py [Arquivo/Caminho do arquivo] [valor da chave] modo [enc/ENC encriptar dec/DEC decifrar] \n \n'
      'Exemplo de encriptação: python3 cesar.py /home/documents/plaintext.txt 5 enc \n'
      'Exemplo para decifrar: python3 cesar.py /home/documents/ciphertext.txt 5 dec')

# file = open(sys.argv[1],'r').read().lower()
# key = int(sys.argv[2])
# mode = sys.argv[3]
# resultado = ''

if len(sys.argv) != 3:
    help()
    exit(0)


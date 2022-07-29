import sys
import calculo_cifra


file = open(sys.argv[1], 'r').read().lower()
key = int(sys.argv[2])
mode = sys.argv[3]

try:
    if mode == 'enc' or mode == 'ENC':
        calculo_cifra.encrypt(file, key)
    elif mode == 'dec' or mode == 'DEC':
        calculo_cifra.decrypt(file, key)
except:
    raise
    calculo_cifra.help()
    exit(0)


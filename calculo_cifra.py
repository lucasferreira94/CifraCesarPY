from string import ascii_lowercase as lc


def help():
    print('Modo de uso: \n'
      'python3 cesar.py [Arquivo/Caminho do arquivo] [valor da chave] modo [enc/ENC encriptar dec/DEC decifrar] \n \n'
      'Exemplo para encriptar: python3 cesar.py /home/documents/plaintext.txt 5 enc \n'
      'Exemplo para decifrar: python3 cesar.py /home/documents/ciphertext.txt 5 dec \n'
      'Exemplo para realizar Brute Force: python3 brute_force.py /home/documetns/ciphertext.txt')

def encrypt(file, key):
    resultado = ''
    index = 0
    for linha in file:
        for letra in linha:
            if letra in lc:
                index = lc.find(letra)
                index = (index + key) % 26
                resultado += lc[index]
            else:
                resultado += letra
    file2 = open('ciphertext.txt', 'a+')
    file2.write(resultado + ' ')
    file2.close()


def decrypt(file, key):
    resultado = ''
    index = 0
    for linha in file:
        for letra in linha:
            if letra in lc:
                index = lc.find(letra)
                index = (index - key) % 26
                resultado += lc[index]
            else:
                resultado += letra
    file2 = open('plaintext.txt', 'a+')
    file2.write(resultado + ' ')
    file2.close()

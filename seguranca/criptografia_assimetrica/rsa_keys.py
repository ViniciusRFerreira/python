import argparse
from binhex import openrsrc
from curses import KEY_RESIZE
import rsa

def generateKeys(file_pub, file_priv,keysize = 1024):
    (publicKey, privateKey) = rsa.newkeys(KEY_SIZE)
    with open(file_pub, 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open(file_priv, 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    #nome padrão do arquivo
    FILE_PRIV = 'privateKey.pem'
    FILE_PUB = 'publicKey.pem'
    KEY_SIZE = 1024


    parser.add_argument('-u','--user')
    parser.add_argument('-v','--verbose', action='store_true')
    parser.add_argument('-s','--keysize', type=int ,choices=[1024, 2048, 4096])


    args = parser.parse_args()

    if args.user:
        FILE_PRIV = f'{args.user}_{FILE_PRIV}'
        FILE_PUB = f'{args.user}_{FILE_PUB}'

    if args.keysize:
        KEY_SIZE = args.keysize

    if args.verbose:
        print(f'Chave pública: {FILE_PUB}')
        print(f'Chave privada: {FILE_PRIV}')
        print(f'Tamanho da chave: {KEY_SIZE}')

    #gera as chaves
    generateKeys(FILE_PUB,FILE_PRIV, KEY_SIZE)
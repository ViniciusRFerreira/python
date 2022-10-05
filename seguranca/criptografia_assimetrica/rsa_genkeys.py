# Vinícius R. Ferreira

import rsa
import argparse

#Para executar:
#rsa_genkeys -u USER -s SIZE -v

def generate_keys(user, keysize):
    #Utilize estes nomes de arquivo para armazenar as chaves
    FILE_PUBLIC_KEY = f'{user}_publib_key.pem'
    FILE_PRIVATE_KEY = f'{user}_private_key.pem'
    
    (public_key, private_key) = rsa.newkeys(keysize)

    #Inclua aqui o código para geração de chaves
    with open(FILE_PUBLIC_KEY, 'wb') as p:
        p.write(public_key.save_pkcs1("PEM"))

    with open(FILE_PRIVATE_KEY, 'wb') as p:
        p.write(private_key.save_pkcs1("PEM"))

if __name__ == '__main__':

    #Default values
    USER='user'
    KEYSIZE = 1024

    parser = argparse.ArgumentParser()

    parser.add_argument('-u', '--user',
        help='Usuário a ter o nome no arquivo da chave.',
        type=str
        )
    parser.add_argument('-s', '--keysize',
        help='Tamanho da chave a ser utilizado.',
        type=int,
        choices=[512, 1024, 2048, 4096]
        )
    parser.add_argument('-v', '--verbose',
        help='Apresenta informações sobre a operação',
        action='store_true'
        )

    args = parser.parse_args()

    if args.user:
        USER=args.user
    if args.keysize:
        KEYSIZE = args.keysize

    if args.verbose:
        print(f'FILE_PUBLIC_KEY: {USER}_publib_key.pem')
        print(f'FILE_PRIVATE_KEY: {USER}_private_key.pem')
        print(f'KEYSIZE: {KEYSIZE}')

    generate_keys(USER,KEYSIZE)

from Crypto.Hash import SHA256, MD5, SHA224, SHA512
import argparse

md5 = MD5
sha224 = SHA224
sha256 = SHA256
sha512 = SHA512

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--alg', type =str, help='Algoritmo de calculo hash.', choices=['md5', 'sha224', 'sha256', 'sha512'])
parser.add_argument('-f', '--alg', type =str, help='Tester', choices=['md5', 'sha224', 'sha256', 'sha512'])

args = parser.parse_args()

if args.alg:
    print(f'Algoritmo escolhido: {args.alg}')

    if args.alg == 'md5':
        a = open('dados.txt','r')
        t = a.read()
        print(a.read())
        hash = MD5.new(data = t.encode())
        print(hash.hexdigest())

    if args.alg == 'sha224':
        a = open('dados.txt','r')
        t = a.read()
        print(a.read())
        hash = SHA224.new(data = t.encode())
        print(hash.hexdigest())

    if args.alg == 'sha256':
        a = open('dados.txt','r')
        t = a.read()
        print(a.read())
        hash = SHA256.new(data = t.encode())
        print(hash.hexdigest())

    if args.alg == 'sha512':
        a = open('dados.txt','r')
        t = a.read()
        print(a.read())
        hash = SHA512.new(data = t.encode())
        print(hash.hexdigest())

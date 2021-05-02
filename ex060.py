'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''
'''import math as mt
n1 = int(input('Digite um número: '))
print('O valor de {}! é = {}.'.format(n1,mt.factorial(n1)))'''
n = int(input('Digite um número:'))
c = n
f = 1
while c > 0:
    print('{}'.format(c),end=' ')
    print('x' if c > 1 else '=',end=' ')
    f*=c
    c -= 1
print(f)
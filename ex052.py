#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
from colorama import Fore
num = int(input('Digite um número: '))
tot = 0
for c in range( 1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot +=1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\33[m0{}'.format(tot))
if tot ==2:
    print('o número {} foir dividido {} vezes, portanto é primo'.format(num,tot))
else:
    print('Não é primo')
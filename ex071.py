'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

'''valor= int(input('valor '))
cedulas = valor // 50
resto = valor%50
print(cedulas)
print(resto)
if cedulas > 0:
    print(f'{cedulas} notas de 50')
cedulas = resto //20
resto%=20
if cedulas> 0:
    print(f'{cedulas} notas de 20')
cedulas = resto // 10
resto%=10
if cedulas > 0:
    print(f'{cedulas} notas de 10')
cedulas = resto // 1
resto%=1
if cedulas > 0:
    print(f'{cedulas} notas de 1')'''
import statistics as sts
import time as tm
op_saque = [100,50,20,10,5,2]

saque = 0
valores = 0
while True:
    saque = int(input('''Qual a sua opção de saque? (Suas opções são:
    [ 0 ] + 100

    [ 1 ] + 50

    [ 2 ] + 20

    [ 3 ] + 10

    [ 4 ] + 5
    
    [ 5 ] + 2 '''))
    print(f'Nota selecionada {op_saque[saque]}')
    lista = op_saque[saque]
    valores += lista
    print(f'Total R$ {valores}')

    saque_mais = ' '
    while saque_mais not in 'SN':
        saque_mais = str(input('Quer sacar mais? [S/N]').upper())
    if saque_mais == 'N':
        break
print('Confirmando valor...')
tm.sleep(1)
print(f'Total que será sacado R$ {valores}')
print('Contando notas...')
tm.sleep(1)
cedulas = valores // 100
resto = valores%100
if cedulas > 0:
    print(f'{cedulas} notas de 100')
cedulas = resto //50
resto%=50
if cedulas> 0:
    print(f'{cedulas} notas de 50')
cedulas = resto // 20
resto%=20
if cedulas > 0:
    print(f'{cedulas} notas de 20')
cedulas = resto // 10
resto%=10
if cedulas > 0:
    print(f'{cedulas} notas de 10')
cedulas = resto // 5
resto %= 5
if cedulas > 0:
    print(f'{cedulas} notas de 5')
cedulas = resto // 2
resto%=2
if cedulas > 0:
    print(f'{cedulas} notas de 2')
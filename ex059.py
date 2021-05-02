'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('Os números que você escolheu foram: {} , {}.'.format(n1,n2))
op = 0
while op !=5:
    print('''Suas opções são:
    [ 1 ] somar
    
    [ 2 ] multiplicar
    
    [ 3 ] maior
    
    [ 4 ] novos números
    
    [ 5 ] sair do programa''')
    op = int(input('Qual a opção que deseja? '))
    if op == 1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))
    elif op ==2:
        print('{} * {} = {}'.format(n1,n2,n1*n2))
    elif op == 3:
        print('o maior número entre {} e {} é {}'.format(n1,n2,max(n1,n2)))
    elif op ==4:
        n1 = int(input('Digite novamente: '))
        n2 = int(input('Digite novamente: '))
    else:
        print('Opção inválida')
    sleep(2)

print('Você saiu do loop, pois a condição se tornou Falsa')

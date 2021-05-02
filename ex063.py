'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8'''
print('-='*30)
n = int(input("Quantos termos deseja encontrar: "))
print('-='*30)
ultimo = 1
penultimo = 0
cont = 3
print('{} -> {}'.format(penultimo, ultimo),end=' ')
while cont <=n:
    termo = ultimo + penultimo
    penultimo =ultimo
    ultimo=termo
    cont+=1
    print('-> {}'.format(termo),end=' ')


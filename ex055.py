#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
import math
lista = []
for pessoa in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(pessoa)))
    lista += [peso]
print(lista)
print('o maior valor foi {} e o menor foi {}'.format(max(lista),min(lista)))


'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
print('{:-^30}'.format('LOJA SUPER BARATÃO'))
tot1000 = s = menor  = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    valor = int(input('Preço: R$ '))
    cont += 1
    s += valor

    if valor >= 1000:
        tot1000 +=1
    if cont == 1 or valor < menor:
        menor = valor
        barato  = produto

    req = ' '
    while req not in 'SN':
        req = str(input('Quer continuar? ').upper())
    if req == 'N':
        break
print(f'O total da compra deu R$ {s:.2f}.\nProdutos cadastros mais caros que R$ 1000: {tot1000}. \nO produto mais barato foi {barato}, que custou {menor} ')

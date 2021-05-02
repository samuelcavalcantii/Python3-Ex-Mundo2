'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
s = n = 0
while n != 999:
    n = int(input('digite um valor '))
    if n != 999:
        s+=n
    else:
        n = n
print(s)
print('FIM')

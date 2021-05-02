'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''
tot18 = f = m = 0
while True:
    sexo = ' '
    idade = int(input('Digite a idade: '))

    while sexo not in 'MF':
        sexo = str(input('Digite o Sexo: [M/f] ').upper())
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? [S/N]').upper())
    if idade > 18:
        tot18 +=1
    elif idade < 20 and sexo == 'F':
        f +=1
    elif sexo == 'M':
        m +=1
    if continuar == 'N':
        break
print(f'{tot18} pessoas tem idade maior que 18.\n{f} Mulheres tem idade menor que 20.\n{m} Homens foram cadastrados')


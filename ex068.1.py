#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random as rd
import time
v = 0
d = 0
while True:
    print('=-'*20)
    jogador = int(input('número: '))
    computador = int(rd.randint(0,10))
    soma = jogador + computador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]').upper()[0])
    print(f'Voce jogou {jogador} e o computador jogou {computador}. TOTAL deu {soma}.',end= '')
    print(f'DEU PAR' if soma%2 == 0 else 'DEU IMPAR')
    if tipo == 'p'.upper():
        if soma % 2 == 0:
            print('Você ganhou')
            v +=1
        else:
            print('Você perdeu')
            d += 1
            break
    elif tipo == 'i'.upper():
        if soma % 2 == 1:
            print('Você ganhou')
            v+=1
        else:
            print('Você perdeu')
            d += 1
            break
print(f'Placar: \n Jogador {v} X {d} Computador ')

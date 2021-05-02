#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random as rd
import time
while True:
    print('=-'*20)
    jogador = int(input('número: '))
    tipo = str(input('Par ou Ímpar? [P/I]').upper()[0])
    computador = int(rd.randint(0,10))
    soma = jogador + computador
    if soma%2 == 0:
        print(f'Voce jogou {jogador} e o computador jogou {computador}. TOTAL deu {soma}, que é PAR')
        if tipo == 'p'.upper():
            print('Você venceu!')
        else:
            print('Computador ganhou!')
            print('Jogo Encerrado')
            break
    else:
        print(f'Voce jogou {jogador} e o computador jogou {computador}. TOTAL deu {soma}, que é IMPAR')
        if tipo == 'i'.upper():
            print('Você venceu!')
        else:
            print('Computador ganhou!')
            print('Jogo Encerrado')
            break

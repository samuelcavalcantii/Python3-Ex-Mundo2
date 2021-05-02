from random import randint, choice, shuffle
from time import sleep
from colorama import Fore, Back
jogarNovamente = 's'
print('\/-'*11)
print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
print('-='*11)
itens = ['PEDRA','PAPEL', 'TESOURA']
pc = choice (itens)
jogador = int(input('Qual a sua jogada?'))
#print('¬L'*11)
print('JO...')
sleep (1)
print('KEN...')
sleep (1)
print ('PO!')
print('-='*11)
print('O jogador jogou {}'.format(itens[jogador]))
#sleep(0.5)
print('O pc jogou...{}'.format (pc))
print('-='*11)
#sleep(1)
if pc == itens[0]:
    if jogador ==0:
        print(Fore.YELLOW+'EMPATE!'+Fore.RESET)
    elif jogador ==1:
        print(Fore.GREEN+'VITÓRIA!'+Fore.RESET)
    elif jogador == 2:
        print(Fore.RED+'VOCÊ PERDEU!'+Back.RESET)
elif pc == itens [1]:
    if jogador == 0:
        print('\033[31mVOCÊ PERDEU!\033[31m')
    elif jogador ==1:
        print('\033[33mEMPATE!\033[m')
    elif jogador == 2:
        print('VITÓRIA!')
elif pc == itens [2]:
    if jogador ==0:
        print('VITÓRIA!')
    elif jogador ==1:
        print('\03  3[31mVOCÊ PERDEU!\033[31m')
    elif jogador ==2:
        print('\033[33mEMPATE!\033[m')





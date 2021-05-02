#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
r = int(randint(0,10))
print('''Pensei num número. 
Advinha aí que se tu acertar te dou um xilito de cebola''')
jogar = input('Voce quer jogar? [S/N]'.strip().upper())
palpites = 0
jogayjoga = int(input('Chuta um número: '))
while jogayjoga != r:
    palpites += 1
    if jogayjoga < r:
        print('Um pouco mais.')
        jogayjoga = int(input('Chuta um número: '))
    elif jogayjoga > r:
        print('Um pouco menos..')
        jogayjoga = int(input('Chuta um número: '))


if palpites > 2:
    print('Acertou com {} tentativas. Demorou'.format(palpites))
else:
    print('Acertou com {}. CAGADO'.format(palpites))






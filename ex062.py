'''Exercício Python 62:
 Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''
import time as tm
print('-=-'*10, '\nGerador de PA')
a = int(input('Primeiro Termo: '))
r = int(input('Digite a razão da PA: '))
print('O primeiro termo da PA é {}\ne a razão é {}.'. format(a,r))
termo = a
cont = 1
total = 0
mais = 10

while mais !=0:
    total += mais
    while cont<= total:
        print(termo, end=' ')
        termo +=r
        cont +=1
    print('PAUSA')
    mais = int(input('Quantos termos queres adicionar?'))
print('FIM')
print(total)

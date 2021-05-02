'''Exercício Python 61:
 Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
'''ao = int(input('Primeiro Termo: '))
r = int(input('Digite a razão da PA: '))
a10 = ao + (10 - 1) * r
for n in range(ao,a10 + r, r):
    print(n, end=' --> ')
print('FIM')'''
import time as tm
print('-=-'*10, '\nGerador de PA')
a = int(input('Primeiro Termo: '))
r = int(input('Digite a razão da PA: '))
quant = int(input('Digite a quantidade de PAs '))
print('O primeiro termo da PA é {}\ne a razão é {}.'. format(a,r))
termo = a
cont = 1
tm.sleep(1.5)
while cont<= quant:
    termo += r
    cont +=1
    print(termo, end=' ')
print('FIM')
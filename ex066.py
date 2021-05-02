#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
import time
print('|'+ '=-'*10+'|')
print(' Contador de Números')
print('|'+ '=-'*10+'|')
s = n = c = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        print('Programa Encerrado')
        print('~.'*11)
        break
    s += n
    c += 1
print('Analisando os resultado...')
time.sleep(1)
print(f'Você digitou {c} números e a soma foi: {s}', end = '')
#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
s = c = n=  0
resp = 'S'
valores = []
import statistics as sts
while resp in 'Ss':

    valores.insert(n, int(input('valor: ')))
    s = sum(valores)
    c += 1
    media = s / c
    resp = str(input('Quer continuar?[S/N]'.upper().strip()))
print(valores)
print(s)
print(c)
print(media)
print(max(valores), min(valores))
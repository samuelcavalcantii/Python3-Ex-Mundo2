import time
print('|'+ '=-'*10+'|')
print(' Contador de Números')
print('|'+ '=-'*10+'|')
s = c = n = 0
lista_numeros = []

while True:
    lista_numeros.insert(n, int(input('Digite um número (999 para parar): ')))
    print(lista_numeros)
    if n == 999:
        print('Programa Encerrado')
        print('~.'*11)
        break
    s += n
    c += 1
print('Analisando os resultado...')
time.sleep(1)
print(f'Lista de números {lista_numeros}')

print(f'Você digitou {c} números e a soma foi: {s}', end = '')
#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    print('=-'*40)
    n = int(input('Qual tabuada você quer ver?  '))
    print('=-' * 40)
    if n< 0:
        print('Tabuada encerrada')
        break
    for c in range (1,11):
        print(f'{n} x {c} = {n * c} ')



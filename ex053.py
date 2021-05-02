#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print(frase)
print(palavras)
print(junto)
print(inverso)
print(palavras[0])
inverso = junto[::-1]
print(inverso)
print('A frase inversa de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('É um palindrome')
else:
    print('Não é um palíndromo')

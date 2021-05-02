ao = int(input('Primeiro Termo: '))
r = int(input('Digite a razão da PA: '))
a10 = ao + (10 - 1) * r
for n in range(ao,a10 + r, r):
    print(n, end=' --> ')
print('FIM')
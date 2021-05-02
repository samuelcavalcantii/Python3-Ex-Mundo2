print('Tabuada de um número qualquer.')
n=int(input('Digite um número:'))
"""print(
    '''
    1x{} = {}
    2x{} = {}
    3x{} = {}
    4x{} = {}'''.format(n,n*1,n,n*2,n,n*3,n,n*4))"""
print('A tabuada de {} é: '.format(n))
for c in range (1,11):
    print(n*c)

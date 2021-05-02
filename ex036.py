casa=float(input('Valor da casa: R$'))
salário=float(input('Salário do comprador:'))
anos=int(input('Quantos anos de financiamento?'))
prestação=casa/(anos*12)
def prestacao ():
    global casa
    global salário
    global prestação
    global prestação

    print('Mínimo para comprar uma casa {} $'. format(salário*0.3))
    print('Uma casa de R$ {}, terá uma prestação por mês de {:0.2f} se for paga em {} anos '. format(casa,prestação,anos))
    if prestação <=salário*0.3:
        print('\033[32mCompra aprovada\033[m!')
    else:
        print('\033[31mCompra recusada\033[m.')
    print('Volte sempre!')
while True:
    prestacao()
    break
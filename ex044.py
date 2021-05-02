from colorama import Fore
print('''    ===========================
    =======''' + Fore.LIGHTGREEN_EX + '''LOJAS ALIBABA''' + Fore.RESET + '''=======
    ===========================''')
p=int(input('Preço da compra: R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque 
[2] à vista cartão
[3] 2x no cartão
[4] 3 x ou mais no cartão''')
op=int(input(' Qual a opção de pagamento?'))
if op == 1:
    print(p-p*0.1)
elif op ==2:
    print(p-p*0.05)
elif op==3:
    print(p/2)
elif op==4:
    pa=int(input('Quantas parcelas vão ser?'))
    print((p+p*0.2)/pa)

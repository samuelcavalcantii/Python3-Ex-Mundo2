from colorama import Fore, Back
n1=float(input('PRIMEIRA NOTA:'))
n2=float(input('SEGUNDA NOTA:'))
média=(n1+n2)/2
print('A sua média é {:0.1f}.'.format(média))
if média >= 9:
    print(Fore.BLUE + 'Aprovado' + Fore.RESET)
    print('Parabéns!! NERDÃO.')
elif 7<=média<9:
    print('BOOA! Tá aprovado!')
elif 7 > média >=4:
    print(Fore.RED+ 'RECUPERÇÃO\033[m'+Fore.RESET)
    print('nhem')
else:
    print(Fore.MAGENTA + 'REPROVADO kkkkkkkkkkkk.'+Fore.RESET)
    print('Estude mais!')

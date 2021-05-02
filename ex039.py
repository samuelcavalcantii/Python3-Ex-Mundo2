from datetime import date
atual = date.today().year
nasc=int(input('Ano de nascimento:'))
idade = atual - nasc
saldo=18-idade
saldon=idade - 18
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))
if idade==18:
    print('Seu alistamento é este ano!!!!')
elif idade>18:
    print('Seu alistamento foi em {}.'. format(atual-(saldon)))
else:
    print('Falta(m) {} ano(s) para o seu alistamento'.format(saldo))
    print('Seu alistamento será em {}.'.format(saldo + atual))
print('Até mais.')
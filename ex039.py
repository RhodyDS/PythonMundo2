from datetime import date
atual = date.today().year
b = int(input('insira seu ano de nascimento: '))
a = atual - b

if a == 18:
    print('você está na idade de se alistar.')

elif a < 18:
    print('ainda não está na idade de se alistar.\nfaltam {} para você se alistar'.format(18-a))
elif a >18:
    print('você já passou da idade de se alistar\nja se passaram {} anos do prazo de se alistar'.format(a-18))
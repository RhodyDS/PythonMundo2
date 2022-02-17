from datetime import date
atual = date.today().year
b=0
for i in range(0,7):
    a=int(input('qual a data de nascimento da pessoa numero {}: '.format(i+1)))
    if atual-a>=18:
        b+=1
print('{} pessoas são atingiram maioridade.'.format(b))
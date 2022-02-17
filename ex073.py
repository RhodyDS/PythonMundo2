tabela = ('Atlético-MG','FLA','PAL','FOR','COR','BRG','FLU','AMG','AGO','SAN','CEA','INT','SAO','CAP','CUI','ECJ','GRE','BAH','SPT','CHA')

print('os primeiros colocados da tabela:')
for i in range(0,5):
    print(f'{i+1}° colocação : {tabela[i]}')

print('os ultimos colocados da tabela:')
for i in range(16,20):
    print(f'{i+1}° colocação : {tabela[i]}')
print(sorted(tabela))
print('o time chapecoense está na posição: ',end='')
print(tabela.index('CHA'))


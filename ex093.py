a = input('insira o nome do jogador:')
b = int(input('quantas partidas ele jogou: '))
pt = {}
jogador = {}
for i in range(0,b):
    pt[f'partida {i+1}'] = input(f'quantos gols ele fez na pt {i+1}: ')

jogador[a] = pt

print(jogador)

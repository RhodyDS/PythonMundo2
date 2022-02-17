from random import randint
dado = {}
dado ['jog1'] = randint(1,6)
dado ['jog2'] = randint(1,6)
dado ['jog3'] = randint(1,6)
dado ['jog4'] = randint(1,6)

max_key = max(dado, key = dado.get)
print(max_key)


for i in sorted(dado , key = dado.get):
    print(i, dado [i])




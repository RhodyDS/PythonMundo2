b = []

while True:
    a = int(input('insira um valor [999 para cancelar]:'))
    if a != 999:
        b.append(a)
    else:
        break
print(f'''
a soma entre os valores digitados é de :{sum(b)}
e foram digitados {len(b)} ''')



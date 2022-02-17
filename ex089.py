dado = []
ficha = []

while True:
    dado.append(input('insira o nome: '))
    dado.append(int(input('insira a primeira nota: ')))
    dado.append(int(input('insira a segunda nota: ')))
    ficha.append(dado[:])
    dado.clear()
    s = input('deseja continuar? s-sim (outra tecla)-cancelar')
    if s not in "sS":
        break

for i in range(0,len(ficha)):
    print(f'aluno:{ficha[i][0]}\n{(ficha[i][1]+ficha[i][2])/2}')
resp = input('deseja ver as notas de algum aluno? s- [sim],(outra tecla]-cancela')
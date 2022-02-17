while True:
    a = int(input('digite um valor:'))
    if a <0:
        break
    if a != 0:
        for i in range(1,11):
          print(f'{a} X {i}={a*i}')
    else:
        break
print('tabuada encerrada')
tab = ('feijao',2,'arroz',5,'manga',3,'macarrão',7)

print("-----atacadão-----")
for i in range(0,4):
    if i%2 == 0:
        print(f'{tab[i]:.<30}',end='')
    else:
        print(f'R${tab[i]:>7.2f}')
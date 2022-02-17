import random,time
soma = 0
vit = 0
while True:
    print('JOGO PAR OU IMPAR')
    a = int(input('escolha um numero inteiro.\n'))
    b = int(input('1 - [impar]'
                  ' 2 - [par]'
                  ' 0 - [sair]'))
    print('ANALISANDO...')
    time.sleep(2)
    if b == 0:
        print('tchau tchau')
        break
    elif b != 1 and b != 2:
        print('valor incorreto insira os valores novamente.\n')

    else:

        bot = random.randint(1,10)
        if b == 1:
            soma = bot + a
            if soma % 2==0:
                print('você perdeu!!'
                      f'o bot escolheu par e jogou o numero {bot}')
                print(f'total de vitorias consecutivas: {vit}')
                break
            else:
                print('você ganhou!!'
                      f'fo bot escolher par e jogou o numero {bot}')
                vit += 1
        elif b == 2:
            if soma % 2 == 0:
                print('você Ganhou!!'
                      f'o bot escolheu impar e jogou o numero {bot}')
                vit += 1
            else:
                print('você perdeu!!'
                      f'o bot escolher impar e jogou o numero {bot}')
                print(f'total de vitorias consecutivas: {vit}')
                break

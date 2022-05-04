import random

opcao = 's'

while opcao == 's':

    lista = ['pedra', 'papel', 'tesoura']

    gesto = random.choice(lista)

    gesto2 = input("Digite pedra ou papel ou tesoura: ")
    print(gesto)

    if gesto2 == 'pedra' :

        if gesto == 'pedra':
            print("empate")
            opcao = input('Deseja continuar? s/n: ')
        elif gesto == 'tesoura':
            print("voce venceu")
            opcao = input('Deseja continuar? s/n: ')
        else:
            print("voce perdeu")
            opcao = input('Deseja continuar? s/n: ')

    elif gesto2 == 'tesoura':

        if gesto == 'pedra':
            print('voce perdeu')
            opcao = input('Deseja continuar? s/n: ')
        elif gesto == 'tesoura':
            print('empate')
            opcao = input('Deseja continuar? s/n: ')
        else:
            print("voce venceu")
            opcao = input('Deseja continuar? s/n: ')
    else:
        if gesto == 'pedra':
            print('voce ganhou')
            opcao = input('Deseja continuar? s/n: ')
        elif gesto == 'tesoura':
             print('voce perdeu')
             opcao = input('Deseja continuar? s/n: ')
        else:
            print('empate')
            opcao = input('Deseja continuar? s/n: ')
else:
    print('obrigado por jogar')

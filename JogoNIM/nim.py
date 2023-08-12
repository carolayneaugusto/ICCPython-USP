def usuario_escolhe_jogada(n,m):
    jogada_valida = False

    while not jogada_valida :
        jogada = int(input('\nQuantas peças você vai tirar? '))
        if jogada > m or jogada < 1 or jogada > n:
            print('\nOops! Jogada inválida! Tente de novo.\n')
        else:
            jogada_valida = True
    
    return jogada
            


def computador_escolhe_jogada(n,m):
    retiradas = 0
    if n <= m:
        return n
    else:
        retiradas = (n % (m + 1))
        
        if retiradas > 0:
            return retiradas
        else:
            return


def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogadas? '))

    usuario_comeca = peças_retiradas = 0

    if n % (m + 1) == 0:
        print('\nVocê começa!')
        usuario_comeca = True
    else:
        print('\nComputador começa!')
        usuario_comeca = False

    while n > 0:
        if usuario_comeca:
            peças_retiradas = usuario_escolhe_jogada(n,m)
            usuario_comeca = False
            print(f'\nVocê tirou {peças_retiradas}.')
        else:
            peças_retiradas = computador_escolhe_jogada(n,m)
            usuario_comeca = True
            print(f'\nO computador retirou {peças_retiradas} peças.')
           
        n -= peças_retiradas
        print(f'Apenas restam {n} peças no tabuleiro.')
    
    if n == 0:
        print('Fim do jogo! ', end=' ')
        if usuario_comeca:
            print('Computador ganhou!')
            return 0
        else:
            print('Você ganhou!')
            return 1


def campeonato():
    print('\nVocê escolheu um campeonato!')

    usuario = computador  = 0

    for i in range(1, 4):
        print(f'\n**** Rodada {i} ****')
        vencedor = partida()

        if vencedor == 0:
            computador += 1
        else:
            usuario += 1

    print('\n**** Final do Campeonato! ****')
    
    print(f'Placar: Você {usuario} X {computador} Computador')



print('Bem-vindo ao jogo do NIM! Escolha:\n')
print('1 - para jogar uma partida isolada')
print('2 - para jogar um campeonato')

opção = int(input('Opção: '))

if opção == 1:
    partida()
else:
    campeonato()

    
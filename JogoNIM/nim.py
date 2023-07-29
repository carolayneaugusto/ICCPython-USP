def computador_escolhe_jogada(n, m):
        '''
devolve um inteiro correspondente à próxima jogada do computador (ou seja, quantas peças o computador deve retirar do tabuleiro) de acordo com a estratégia vencedora.
'''




def usuario_escolhe_jogada(n, m):
    '''
solicita que o jogador informe sua jogada e verifica se o valor informado é válido. Se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida. 
'''
    


def partida():
      n = int(input('Quantas peças? '))
      m = int(input('Limite de peças por jogada? '))
      return n, m

def campeonato():
      print('campeonato')
      


print('Bem-vindo ao jogo do NIM! Escolha:')
print('1 - para jogar uma partida isolada')
print('2 - para jogar um campeonato')

escolha = int(input('Opção: '))

if escolha == 1:
      print('Você escolheu uma partida isolada!')
      partida()
elif escolha == 2:
      print('Você escolheu um campeonato!')
      campeonato()
else:
      print('Opção inválida!')

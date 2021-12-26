import random

computador = random.randint(1, 3)
jogador = int(input('''Escolha um:
1 - Pedra
2 - Papel
3 - Tesoura\n'''))

jogadas = ['Pedra', 'Papel', 'Tesoura']

print('Jogador = {}'.format((jogadas[jogador - 1])))
print('computador = {}'.format((jogadas[computador - 1])))

if (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
    print('Ganhou')
elif jogador == computador:
    print('Empate')
else:
    print('Perdeu')


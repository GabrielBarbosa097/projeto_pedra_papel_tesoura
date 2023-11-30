#Criando a parte incial do projeto
import random
nome = str(input('Digite seu nome: '))

while True:
 jogador = str(input(f'{nome}, escolha entre PEDRA|PAPEL|TESOURA: ')).strip().lower()
 lista = ['pedra','papel','tesoura']
 computador = random.choice(lista)

 if computador == 'pedra':
  if jogador == 'pedra':
   print(f'O computador escolheu {computador}, já o jogador {nome} escolheu {jogador}e no final deu empate')
  elif jogador == 'papel':
    print(f'O computador escolheu {computador}, já o jogador {nome} escolheu {jogador}e no final o jogador ganhou')
  elif jogador == 'tesoura':
   print(f'O computador escolheu {computador}, já o jogador {nome} escolheu {jogador}e no final o computador ganhou')
 elif computador == 'papel':
  if jogador == 'pedra':
   print(f'O computador escolheu {computador}, já o jogador {nome} escolheu {jogador}e no final o computador ganhou') 
  elif jogador == 'papel':
   print(f'O computador escolheu {computador}, já o jogador {nome} escolheu {jogador}e no final deu empate')
  elif jogador == 'tesoura':
   print(f'O computador escolheu {computador}, já o jogador {nome} escolheu {jogador}e no final o jogador ganhou')
  elif computador == 'tesoura':
   if jogador == 'pedra':
    print(f'O computador escolheu {computador}, já o jogador {nome} escolheu {jogador}e no final o jogador ganhou')  
   elif jogador == 'papel':
    print(f'O computador escolheu {computador}, já o jogador {nome} escolheu {jogador}e no final o computador ganhou')
   elif jogador == 'tesoura':
    print(f'O computador escolheu {computador}, já o jogador {nome} escolheu {jogador}e no final deu empate')
  else:
   print('Respota invalida, Estou reiniciando o jogo')  
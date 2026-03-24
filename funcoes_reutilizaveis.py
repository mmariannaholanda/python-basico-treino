#APRENDENDO FUNÇÕES REUTILIZÁVEIS PYTHON

PASSO 1
def oi(nome):
  print('Oi, tudo bem?? Vamos aprender funções de phyton!!')
  print('E agora qual o nosso proximo passo?')

oi()

PASSO  2----------------------------------------------------------------
def oi():
  nome=input('Qual o seu nome?')
  print(f'Oi, tudo bem, {nome}? Vamos aprender funções de phyton!!')
  print('E agora qual o nosso proximo passo?')

oi()

PASSO 3- assumindo um parametro------------------------------------------
def oi(nome):
  print(f'Oi, tudo bem, {nome}? Vamos aprender funções de phyton!!')
  print(f'E agora qual o nosso proximo passo, {nome}?')
  print()  # <-- para deixar uma linha em branco sempre que escrever uma função.

oi('mari')

oi('joao')

oi('jorge')

oi('fenando')


PASSO 4- MAIS DE 1 PARAMETRO------------------------------------------------
def oi(nome, idade):
  print(f'Oi, tudo bem, {nome}? Você tem {idade} anos né? Vamos aprender funções de phyton!!')
  print(f'E agora qual o nosso proximo passo, {nome}?')
  print()  # <-- para deixar uma linha em branco sempre que escrever uma função.

oi('mari', 17)

oi('joao',19)

oi('jorge',25)

oi('fenando',20)

PASSO 5- COM NÚMEROS-------------------------------------------------------
def somar(num1,num2):
  return num1 + num2

total = somar(4, 5)
print(f'O resultado da soma é de: {total}')
print()

print(somar(1,4))
print(somar(9,9))
print(somar(4,7))
print(somar(3,6))


PASSO 6- INTERAÇÃO COM O USUÁRIO--------------------------------------------
#porcentagem

preco = float(input('Qual o valor inicial? '))
porcentagem = float(input('Qual o desconto você conseguiu? '))

def calcular_desconto(preco,porcentagem):
  valor_final = preco - ((preco*porcentagem)/ 100)
  print()
  print(f'O valor com {porcentagem} de desconto fica apenas {valor_final:.2f}')

calcular_desconto(preco,porcentagem)

--------------------------------------------------------------------------
-------------------------------



































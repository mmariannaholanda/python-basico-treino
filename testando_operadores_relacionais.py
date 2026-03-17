#Testando operadores relacionais
num1=10
num2=10
num3=15

print("Testando operadores relacionais:")
print(num1==num2)
print(num1==num3)
print(num1!=num3)
print(num1>num2)

print("Pondo em prática:")

#Igual ou maior de 18 anos de idade é adulto
idade=int(input("Qual a sua idade? "))

verificador= idade > 18

if verificador==True:
  print("Você é maior de idade!")
else :
  print("Você ainda não é um maior de idade")

#Agora,  vamos fazer um jogo de adivinhe o número
#jogoadvinhe o número

import random

numero = random.randint(1,100)
rodadas = int(input("Quantas rodadas você quer? "))
palpite2 = 0
palpite3 = 0
palpite4 = 0
palpite5 = 0

#rodada 1

palpite1 = int(input("Qual o número entre 1 e 100 você acha que é? "))

if palpite1>numero:
  print("Seu número é maior")
elif palpite1==numero:
  print("Você acertou. Parabéns!!")
else:
  print("Seu número é menor")

#segunda rodada se tiver errado

if palpite1 != numero:

  if rodadas>=2:

    palpite2 = int(input("Tente novamente. Qual o número você quer tentar agora? "))
  
    if palpite2 > numero:
      print("Seu número é maior")
    elif palpite2 == numero:
      print("Você acertou. Parabéns!!")
    else:
      print("Seu número é menor")

  else:
    print(f"Suas rodadas acabram. Você quase chegou lá! O número era {numero}.")

#terceira rodada se tiver errado

if palpite2 != numero:

  if rodadas>=3:

    palpite3 = int(input("Tente novamente. Qual o número você quer tentar agora? "))
  
    if palpite3 > numero:
      print("Seu número é maior")
    elif palpite3 == numero:
      print("Você acertou. Parabéns!!")
    else:
      print("Seu número é menor")
      
  else:
    print(f"Suas rodadas acabram. Você quase chegou lá! O número era {numero}.")

#quarta rodada se tiver errado

if palpite3 != numero:

  if rodadas>=4:

    palpite4 = int(input("Tente novamente. Qual o número você quer tentar agora? "))
  
    if palpite4 > numero:
      print("Seu número é maior")
    elif palpite4 == numero:
      print("Você acertou. Parabéns!!")
    else:
      print("Seu número é menor")

  else:
    print(f"Suas rodadas acabram. Você quase chegou lá! O número era {numero}.")

#quinta rodada se tiver errado

if palpite4 != numero:

  if rodadas>=5:

    palpite5 = int(input("Tente novamente. Qual o número você quer tentar agora? "))
  
    if palpite5 > numero:
      print("Seu número é maior")
    elif palpite5 == numero:
      print("Você acertou. Parabéns!!")
    else:
      print("Seu número é menor")
      
  else:
    print(f"Suas rodadas acabram. Você quase chegou lá! O número era {numero}.")


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

#ATUALIZANDO COM O RECURSO "AND" E 10 RODADAS-------------------------------------------------------------"

import random

numero = random.randint(1, 100)
rodadas = int(input("Quantas rodadas você quer? (até 10) "))
palpite1 = 0
palpite2 = 0
palpite3 = 0
palpite4 = 0
palpite5 = 0
palpite6 = 0
palpite7 = 0
palpite8 = 0
palpite9 = 0
palpite10 = 0

# rodada 1
if rodadas >= 1:
    palpite1 = int(input("Qual o número entre 1 e 100 você acha que é? "))
    if palpite1 > numero:
        print("Seu número é maior")
    elif palpite1 == numero:
        print("Você acertou. Parabéns!!")
    else:
        print("Seu número é menor")
# rodada 2
if palpite1 != numero and rodadas >= 2:
    palpite2 = int(input("Tente novamente: "))
    if palpite2 > numero:
        print("Seu número é maior")
    elif palpite2 == numero:
        print("Você acertou. Parabéns!!")
    else:
        print("Seu número é menor")
# rodada 3
if palpite1 != numero and palpite2 != numero and rodadas >= 3:
    palpite3 = int(input("Tente novamente: "))
    if palpite3 > numero:
        print("Seu número é maior")
    elif palpite3 == numero:
        print("Você acertou. Parabéns!!")
    else:
        print("Seu número é menor")
# rodada 4
if palpite1 != numero and palpite2 != numero and palpite3 != numero and rodadas >= 4:
    palpite4 = int(input("Tente novamente: "))
    if palpite4 > numero:
        print("Seu número é maior")
    elif palpite4 == numero:
        print("Você acertou. Parabéns!!")
    else:
        print("Seu número é menor")
# rodada 5
if palpite1 != numero and palpite2 != numero and palpite3 != numero and palpite4 != numero and rodadas >= 5:
    palpite5 = int(input("Tente novamente: "))
    if palpite5 > numero:
        print("Seu número é maior")
    elif palpite5 == numero:
        print("Você acertou. Parabéns!!")
    else:
        print("Seu número é menor")
# rodada 6
if palpite1 != numero and palpite2 != numero and palpite3 != numero and palpite4 != numero and palpite5 != numero and rodadas >= 6:
    palpite6 = int(input("Tente novamente: "))
    if palpite6 > numero:
        print("Seu número é maior")
    elif palpite6 == numero:
        print("Você acertou. Parabéns!!")
    else:
        print("Seu número é menor")
# rodada 7
if palpite1 != numero and palpite2 != numero and palpite3 != numero and palpite4 != numero and palpite5 != numero and palpite6 != numero and rodadas >= 7:
    palpite7 = int(input("Tente novamente: "))
    if palpite7 > numero:
        print("Seu número é maior")
    elif palpite7 == numero:
        print("Você acertou. Parabéns!!")
    else:
        print("Seu número é menor")
# rodada 8
if palpite1 != numero and palpite2 != numero and palpite3 != numero and palpite4 != numero and palpite5 != numero and palpite6 != numero and palpite7 != numero and rodadas >= 8:
    palpite8 = int(input("Tente novamente: "))
    if palpite8 > numero:
        print("Seu número é maior")
    elif palpite8 == numero:
        print("Você acertou. Parabéns!!")
    else:
        print("Seu número é menor")
# rodada 9
if palpite1 != numero and palpite2 != numero and palpite3 != numero and palpite4 != numero and palpite5 != numero and palpite6 != numero and palpite7 != numero and palpite8 != numero and rodadas >= 9:
    palpite9 = int(input("Tente novamente: "))
    if palpite9 > numero:
        print("Seu número é maior")
    elif palpite9 == numero:
        print("Você acertou. Parabéns!!")
    else:
        print("Seu número é menor")
# rodada 10
if palpite1 != numero and palpite2 != numero and palpite3 != numero and palpite4 != numero and palpite5 != numero and palpite6 != numero and palpite7 != numero and palpite8 != numero and palpite9 != numero and rodadas >= 10:
    palpite10 = int(input("Tente novamente: "))
    if palpite10 > numero:
        print("Seu número é maior")
    elif palpite10 == numero:
        print("Você acertou. Parabéns!!")
    else:
        print("Seu número é menor")
# derrota final
if ( palpite1 != numero and palpite2 != numero and palpite3 != numero and palpite4 != numero and
    palpite5 != numero and palpite6 != numero and palpite7 != numero and palpite8 != numero and
    palpite9 != numero and palpite10 != numero ):
    print(f"Suas rodadas acabaram. Você quase chegou lá! O número era {numero}.")

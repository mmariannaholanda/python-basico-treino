#Criação de lista de números pelo usuário.

numeros= []
continuar= 's'

while continuar == 's':
    num=int(input('Qual número deseja adicionar? '))
    numeros.append(num)

    if len(numeros)==1:
      print(f'Há {len(numeros)} número na sua lista até agora.')
    else:
      print(f'Há {len(numeros)} números na sua lista até agora.')

    continuar = input('Quer continuar? (s/n) ').lower()


print('Você acabou as modificações da lista.')
print('Lista final:')
print(numeros)

maior = numeros[0]
menor = numeros[0]

soma=0

for n in numeros:
    soma+= n

    if n > maior:
        maior = n

    if n < menor:
        menor = n

print(f'Soma dos números: {soma}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')

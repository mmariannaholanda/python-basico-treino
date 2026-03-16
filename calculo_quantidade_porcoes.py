#Calcularemos quantos dias um produto duraria se a pessoa usar x porções por dia

volume=float(input('Quantas porções o produto tem: '))
distribuicao=int(input('Quantas porções você usa por dia? '))
calculodias=(volume/distribuicao)

print(f'O produto durará {calculodias:.0f} dias!')

#testando de novo com outro recurso

print(f'O produto durará {int(calculodias)} dias!')

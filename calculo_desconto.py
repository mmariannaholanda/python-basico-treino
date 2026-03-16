valorI = float(input("Qual o valor inicial: "))
desconto = float(input("Qual a porcentagem de desconto deram? "))
calculodesconto = valorI * (desconto / 100)
valorfinal = valorI - calculodesconto

print(f"O valor que você terá que pagar é de {valorfinal} reais")

if desconto < 25:
    print("O desconto foi pequeno!")
elif desconto < 50:
    print("O desconto foi bom!")
else:
    print("Seu desconto foi muito bom!!")

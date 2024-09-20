import os

os.system("cls")

# EXEMPLO 1

profissao = "Motorista"
localidade = "São Paulo"
funcionario = "funcionário público"
valor_compra = 350

if profissao == "professor" and localidade == "rio de janeiro":
    print("Desconto")
else:
    print("Sem desconto")


if profissao == "professor" or localidade == "rio de janeiro":
    print("Desconto")
else:
    print("Sem desconto")


if profissao == "professor" and localidade == "rio de janeiro" or funcionario == "funcionário público" or valor_compra >= 300:
    print("Desconto")
else:
    print("Sem desconto")

# EXEMPLO 2

idade = int(input("Digite sua idade: "))

if not (idade >= 18):
    print("Menor de 18")
else:
    print("Maior de 18")

# Exemplo 3

luz_acesa = False

if not luz_acesa:
    print("Luz apagada")
else:
    print("Luz acesa")

# EXEMPLO 4

n = int(input("NUMERO: "))

if 10 <= n <= 50:
    print("Intervalo")
else:
    print("Fora do intervalo")


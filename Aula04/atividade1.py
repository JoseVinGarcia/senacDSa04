import os

os.system("cls")

# ATIVIDADE 1

resposta = input("Insira F para feminino e M para masculino: ").upper()

if resposta != "":

    genero = resposta[0]

    if genero == "M":
        print("Masculino")
    elif genero == "F":
        print("Feminino")
    else:
        print("Digite o certo.")
else:
    print("Em branco não pode.")

import random
import string

caracteres = ''
senha = ''

tamanho = int(input("Qual o tamanho desejado para a senha?\n"))

while True:
    escolha = input("\nDeseja utilizar letras minúsculas? (y/n)\n")

    if escolha == 'y':
        caracteres += string.ascii_lowercase
        print("✅")
        break
        
    elif escolha == 'n':
        print("✅")
        break

    else:
        print("❌ Por favor, digite y (sim) ou n (não).")

while True:

    escolha = input("\nDeseja utilizar letras maiúsculas? (y/n)\n")

    if escolha == 'y':
        caracteres += string.ascii_uppercase
        print("✅")
        break

    elif escolha == 'n':
        print("✅")
        break

    else:
        print("❌ Por favor, digite y (sim) ou n (não).")

while True:

    escolha = input("\nDeseja utilizar números? (y/n)\n")

    if escolha == 'y':
        caracteres += string.digits
        print("✅")
        break

    elif escolha == 'n':
        print("✅")
        break

    else:
        print("❌ Por favor, digite y (sim) ou n (não).")

while True:
        
    escolha = input("\nDeseja utilizar símbolos? (y/n)\n")

    if escolha == 'y':
        caracteres += string.punctuation
        print("✅")
        break

    elif escolha == 'n':
        print("✅")
        break

    else:
        print("❌ Por favor, digite y (sim) ou n (não).")

for i in range(tamanho):
    senha += random.choice(caracteres)

print(senha)
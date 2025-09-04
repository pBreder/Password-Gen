import random
import string
from pydrive2.auth import GoogleAuth # Responsavel pela autenticação da conta Google
from pydrive2.drive import GoogleDrive # Responsável pelas interações com o Google Drive

def ini_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() # Responsável pelo site de login na conta Google
    drive = GoogleDrive(gauth) # Responsável por criar um cliente, o qual foi autenticado nas etapas anteriores

    return drive

def cria_pasta(drive, nome_pasta):
    
    pasta = drive.CreateFile({ # Cria uma pasta (Opcional. E, pode ser feito diretamente dentro do bloco da criação do arquivo)
        'title': nome_pasta,
        'mimeType':'application/vnd.google-apps.folder'
    })
    pasta.Upload()
    return pasta['id']

def upload_arquivo(nome_arq, servico, senha):

    drive = ini_drive()

    nome_pasta = input("Insira o nome da sua pasta:\n")

    while True:
        if not nome_pasta.strip():
            print("❌ Por favor, insira o nome da pasta.")
        else:
            break

    lista_pastas = drive.ListFile({'q':f"title = '{nome_pasta}' and mimeType = 'application/vnd.google-apps.folder'"}).GetList()

    if lista_pastas:
        print(f"\nPasta {nome_pasta} encontrada!")
        id_pasta = lista_pastas[0]['id']

    else:
        id_pasta = cria_pasta(drive, nome_pasta)

    lista_arquivos = drive.ListFile({'q':f"title = '{nome_arq}' and '{id_pasta}' in parents"}).GetList()

    if lista_arquivos:
        print(f"Arquivo {nome_arq} encontrado!")
        arquivo = lista_arquivos[0]
        conteudo_arquivo = arquivo.GetContentString()

        atualizacao_conteudo = conteudo_arquivo + f'{servico} ---> {senha}\n'

        arquivo.SetContentString(atualizacao_conteudo) # 'preenche' o arquivo com a nova string
        arquivo.Upload() # Atualiza o arquivo no Drive

    else:
        arquivo = drive.CreateFile({ # Cria um arquivo no drive
            'title':nome_arq,
            'parents':[{'id':id_pasta}],
        })
    
        arquivo.SetContentString(f"{servico} ---> {senha}\n") # 'preenche' o arquivo criado com a senha 
        arquivo.Upload() # Sobe o arquivo para o drive

def salvar_localmente(servico, senha):

    while True:
        nome_arq = input("Insira o nome o arquivo:\n")
        if not nome_arq.strip():
            print("❌ Por favor, insira o nome do arquivo.")
        else:
            break

    with open(f"{nome_arq}.txt", "a") as file:
        file.write(f"{servico} ---> {senha}\n")

    return nome_arq

caracteres = ''
senha = ''

while True:
    servico = input("\nPara qual serviço será sua senha?\n").capitalize()

    if not servico.strip():
        print("❌ Por favor, insira o nome do aplicativo/site/serviço que estará utilizando.")
    else:
        break

while True:
    try:
        tamanho = int(input("\nQual o tamanho desejado para a senha?\n"))
        break
    except ValueError:
        print("❌ Por favor, insira somente números inteiros")

while True:
    escolha = input("\nDeseja utilizar letras minúsculas? (y/n)\n").lower()

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

    escolha = input("\nDeseja utilizar letras maiúsculas? (y/n)\n").lower()

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

    escolha = input("\nDeseja utilizar números? (y/n)\n").lower()

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
        
    escolha = input("\nDeseja utilizar símbolos? (y/n)\n").lower()

    if escolha == 'y':
        caracteres += string.punctuation
        print("✅")
        break

    elif escolha == 'n':
        print("✅\n")
        break

    else:
        print("❌ Por favor, digite y (sim) ou n (não).")

if not caracteres:
    raise ValueError("Deve-se colocar ao menos um tipo de caractere")

for i in range(tamanho):
    senha += random.choice(caracteres)

while True:
    
    localmente = input('Deseja gerar um arquivo registrando a senha em seu computador? (y/n)\n').lower()

    if localmente == 'y':
        nome_arquivo = salvar_localmente(servico, senha)
        print('✅ Arquivo salvo!\n')
        break

    elif localmente == 'n':
        print('✅ O arquivo não foi salvo em seu computador.\n')
        nome_arquivo = ''
        break

    else:
       print("❌ Por favor, digite y (sim) ou n (não).\n")

while True:

    usar_drive = input('Deseja gerar um arquivo registrando a senha em seu Drive? (y/n)\n').lower()

    if usar_drive == 'y':
        upload_arquivo(nome_arquivo, servico, senha)
        print('✅ Upload concluído!\n')
        break

    elif usar_drive == 'n':
        print('✅ Drive não utilizado.\n')
        break

    else:
       print("❌ Por favor, digite y (sim) ou n (não).\n")
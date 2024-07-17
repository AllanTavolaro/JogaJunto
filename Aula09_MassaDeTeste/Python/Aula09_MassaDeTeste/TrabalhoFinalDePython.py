import requests
from faker import Faker 
import json

# Inicializa o gerador de dados do faker com configuração para o português do Brasil
fake = Faker('pt_BR')

# Função para enviar dados usando uma requisição POST
def enviar_dados_post(url, dados):
    # Faz uma requisição POST para a URL fornecida com os dados fornecidos e retorna a resposta
    response = requests.post(url, data=dados)
    return response

# Função para processar a resposta da requisição
def processar_resposta(response):
    # Verifica se a resposta foi bem-sucedida, ou seja, se o código de status é 200 ou 201
    if response.status_code == 200 or response.status_code == 201:
        return response.json()  # Retorna o conteúdo da resposta em formato JSON
    else:
        # Exibe uma mensagem de erro com o código de status se a requisição falhar
        print(f'Erro na requisição: {response.status_code}')
        return None

# Função para salvar dados JSON em um arquivo
def save_json(dados_json, nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as file: 
            # Escreve os dados JSON no arquivo, formatados com uma indentação de 4 espaços
            json.dump(dados_json, file, indent=4)
            print(f"Resposta salva em '{nome_arquivo}'.")
    except IOError as e:
        # Exibe uma mensagem de erro se houver um problema ao salvar o arquivo
        print(f"Erro ao salvar o arquivo: {e}")

# Gera dados fictícios para a criação de um usuário
dados ={
    "username": fake.user_name(),
    "email": fake.email(),
    "password": fake.password(length=10),
    "phone": fake.cellphone_number(),
    "address": fake.address(),
    "cpf": fake.cpf()
}

# Extrai o email e a senha dos dados do usuário para usar no login
dados_login = {
    "email": dados["email"],
    "password": dados["password"]
}

# URLs das APIs para criação de usuário e login
url_create_user = "https://desafiopython.jogajuntoinstituto.org/api/users/"
url_login = "http://desafiopython.jogajuntoinstituto.org/api/users/login/"

#---------- Criação de usuário ----------
# Envia os dados do usuário para a URL de criação e guarda a resposta
resposta_create = enviar_dados_post(url= url_create_user, dados= dados)

# Processa a resposta da criação do usuário
dados_json_create = processar_resposta(response= resposta_create)

# Salva a resposta da criação do usuário em um arquivo de texto
save_json(dados_json= dados_json_create, nome_arquivo= 'resposta_create.txt')

#--------- Login de usuário --------------
# Envia os dados de login para a URL de login e guarda a resposta
resposta_login = enviar_dados_post(url= url_login, dados= dados_login)

# Processa a resposta do login
dados_json__login = processar_resposta(response= resposta_login)

# Salva a resposta do login em um arquivo de texto
save_json(dados_json= dados_json__login, nome_arquivo= 'resposta_login.txt')
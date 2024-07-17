import requests

def consultar_cep(cep):
    # Monta a URL da API com o CEP fornecido
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    # Faz a requisição GET para a API do ViaCEP
    response = requests.get(url)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        
        # Verifica se o CEP foi encontrado
        if 'erro' not in data:
            logradouro = data['logradouro']
            print(f"CEP encontrado! Logradouro: {logradouro}")
        else:
            print("CEP não encontrado.")
    else:
        print(f"Erro ao consultar o CEP. Status Code: {response.status_code}")

def main():
    cep = input("Digite o CEP para consultar (somente números): ")
    consultar_cep(cep)

if __name__ == "__main__":
    main()
import requests

estado_desconto = ["AL", "BA", "CE", "MA", "PE", "PI", "RN", "SE", "AC", "AP", "AM", "PA", "RO", "RR", "TO"]

cep_teste = [
    '01001-000', # São Paulo, SP (Sudeste)
    '20040-002', # Rio de Janeiro, RJ (Sudeste)
    '60060-080', # Fortaleza, CE (Nordeste)
    '30140-071', # Belo Horizonte, MG (Sudeste)
    '40020-000', # Salvador, BA (Nordeste)
    '72000-000', # Brasília, DF (Centro-Oeste)
    '78048-000', # Cuiabá, MT (Centro-Oeste)
    '11630-346', # Ilhabela, SP (Sudeste)
    '69010-060', # Manaus, AM (Norte)
    '09051-160', # Santo André, SP (Sudeste)
    '75000-000', # Anápolis, GO (Centro-Oeste)
    '69900-060', # Rio Branco, AC (Norte)
    '87020-025', # Maringá, PR (Sul)
    '89890-000', # Xanxerê, SC (Sul)
    '90000-000'  # Porto Alegre, RS (Sul)
]

for cep in cep_teste:
    url = f'https://viacep.com.br/ws/{cep}/json/'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'erro' not in data:
                estado = data["uf"]
                elegivel = estado in estado_desconto
                print(f'CEP: {cep}, Elegível para frete grátis: {elegivel}')
            else:
                print(f'CEP: {cep}, Erro: CEP não encontrado')
        else:
            print(f'CEP: {cep}, Erro: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar API ViaCEP: {e}")
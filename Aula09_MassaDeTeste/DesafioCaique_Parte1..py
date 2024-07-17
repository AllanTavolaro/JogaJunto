import pandas as pd

dados = {
    "nome": ["kethanny", "andrea", "sara", "nhaty", "neia", "pedro", "acaue"],
    "idade": [21,40,20,24,38,13,23],
    "cidade": ["Recife", "Salvador", "São Paulo", "Manaus", "Recife", "Salvador", "Recife"]

}

df = pd.DataFrame(data=dados)

print(df)

df_recife = df[df['cidade'] == 'Recife']

print(df_recife)
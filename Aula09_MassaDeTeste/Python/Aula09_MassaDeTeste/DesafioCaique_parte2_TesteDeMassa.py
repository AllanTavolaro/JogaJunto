import pandas as pd


dados = pd.read_csv('dados_ficticios.csv')


df = pd.DataFrame(dados)


print("Pessoas com idade maior ou igual a 40 anos:")
print(df[df['idade'] >= 40])


renda_minima_5mil = 5000
print("\nPessoas com renda maior que 5 mil:")
print(df[df['renda'] > renda_minima_5mil])


renda_minima_15mil = 15000
print("\nPessoas com renda maior que 15 mil:")
print(df[df['renda'] > renda_minima_15mil])
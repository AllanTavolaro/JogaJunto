linguagens_tupla = ('ovos', 'leite', 'trigo', 'fermento', 'oleo')


linguagens_lista = list(linguagens_tupla)
print("Tupla transformada em lista")

print(type(linguagens_lista))


linguagens_lista.extend(["laranja", "agua"])
print("Lista com dois dados adicionados")
print(linguagens_lista)


linguagens_lista.pop(0)


print("Lista com agua removido")
print(linguagens_lista)

print("Primeiro elemento:")
print(linguagens_lista[0])


print("Quantidade de  elementos:")
print(len(linguagens_lista))



dicionario = {
    "Nome": "allan",
    "Idade": 21,
    "Profissão": "Engenheiro de Software"
}

print(dicionario["Nome"])
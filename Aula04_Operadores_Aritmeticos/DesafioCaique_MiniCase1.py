nome = input("Por favor, digite o nome do cachorro: ")
idade = int(input("Digite a idade do cachorro em anos: "))

idadepet = idade * 7
print(f"A idade de {nome} em anos de cachorro é: {idadepet} anos")

def obter_porte_do_cachorro():
    while True:
        porte = input("Por favor, insira o porte do cachorro (pequeno, médio, grande): ").strip().lower()
        if porte in ["pequeno", "medio", "grande"]:
            
            if porte == "medio":
                porte = "médio"
            return porte
        else:
            print("Entrada inválida. Por favor, insira uma das opções: pequeno, médio ou grande.")


porte_cachorro = obter_porte_do_cachorro()

lucros = {
    "pequeno": 50 - 5,
    "médio": 60 - 15,
    "grande": 75 - 20
}
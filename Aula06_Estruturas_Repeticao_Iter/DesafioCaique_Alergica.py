listafruta = ["maca", "banana", "uva", "pera", "manga", "pessego"]
listaalergia = []

listaalergia.append(input("Digite uma fruta que você tenha alergia: ").lower())

print("Lista de frutas:", listafruta)
print("Lista de alergias:", listaalergia)

for i in listafruta:
    if i in listaalergia:
        print(f"Temos {listaalergia} no cardápio!")
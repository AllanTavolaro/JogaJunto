def parimpar(matricula):
    if matricula % 2 == 0:
        print('VOCÊ ESTÁ NO TIME AZUL')
    else:
        print('VOCÊ ESTÁ NO TIME AMARELO')

num_matricula = int(input('Digite o número de sua matricula:'))
parimpar(num_matricula)
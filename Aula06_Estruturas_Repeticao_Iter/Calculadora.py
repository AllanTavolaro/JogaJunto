# Funções para operações matemáticas básicas
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

# Função principal da calculadora utilizando match-case
def calculadora():
        
        print("Escolha a operação q vc deseja. +, -, *, /, ou se deseja sair da calculadora pfvr digite 0")

        opcao = input("Digite a opção desejada: ")

        match opcao:
            case '+':
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                print("Resultado:", soma(num1, num2))
            case '-':
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                print("Resultado:", subtracao(num1, num2))
            case '*':
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                print("Resultado:", multiplicacao(num1, num2))
            case '/':
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                print("Resultado:", divisao(num1, num2))
            case '0':
                print("Calculadora encerrada.")
                return
            case _:
                print("Opção inválida. Tente novamente.")

# Execução da calculadora
calculadora()
# def adicao(x, y):
#     return x + y

# def subtracao(x, y):
#     return x - y

# def multiplicacao(x, y):
#     return x * y

# def divisao(x, y):
#     if y == 0:
#         return "Erro: divisão por zero!"
#     else:
#         return x / y

# print("Selecione a operação:")
# print("1. Adição")
# print("2. Subtração")
# print("3. Multiplicação")
# print("4. Divisão")

# escolha = input("Digite sua escolha (1/2/3/4): ")

# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))

# if escolha == '1':
#     print(num1, "+", num2, "=", adicao(num1, num2))
# elif escolha == '2':
#     print(num1, "-", num2, "=", subtracao(num1, num2))
# elif escolha == '3':
#     print(num1, "*", num2, "=", multiplicacao(num1, num2))
# elif escolha == '4':
#     print(num1, "/", num2, "=", divisao(num1, num2))
# else:
#     print("Opção inválida")


import sys

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: divisão por zero!"
    else:
        return x / y

if(len(sys.argv) != 4):
    print("Sao esperados 3 argumentos, 1: tipo de operacao; 2: valor 1; 3: valor 2")
    exit()

escolha = sys.argv[1]
num1 = int(sys.argv[2])
num2 = int(sys.argv[3])

if escolha == '1':
    print(num1, "+", num2, "=", adicao(num1, num2))
elif escolha == '2':
    print(num1, "-", num2, "=", subtracao(num1, num2))
elif escolha == '3':
    print(num1, "*", num2, "=", multiplicacao(num1, num2))
elif escolha == '4':
    print(num1, "/", num2, "=", divisao(num1, num2))
else:
    print("Opção inválida")
saida = '';

def adicao(a, b):
    return a + b

def subracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return 'Não foi possivel realizar a divisão por 0'
    else:
        return a / b
def calculadora(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"

saida = ''
n = 'n'  # n pode ser trocado por outro valor

while saida.lower() != n:
    primeiro_numero = float(input("Digite o primeiro número: "))
    segundo_numero = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    resultado = calculadora(primeiro_numero, segundo_numero, operacao)

    print('Resultado da operação:', resultado)

    saida = input("Deseja continuar? (s para sim, n para não): ")

print("Programa encerrado.")
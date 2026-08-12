"""
frase = 'O hulk acabou de fazer gol'
print(frase)
print(frase.upper())
print(frase.split())


nome = input("Digite seu time de futebol:")
local = input("Digite o estádio do seu time de futebol:")

print(f"O {nome} joga no estádio {local}")


#----------------------------------------------------------
# EXERCÍCIO SEÇÃO 3 - Variáveis e tipos de dados em python
#----------------------------------------------------------

# 1
numero = 47
print(numero)
print(type(numero))

# 2
digite = int(input("Digite um número inteiro: "))
digite2 = int(input("Digite o segundo número inteiro: "))
digite3 = int(input("Digite o terceiro número inteiro: "))

total = digite + digite2 + digite3

print(f"A soma dos 3 números é {total} ")

# 3
valor1 = 4
valor2 = 8
valor3 = 10

total = valor1**2 + valor2**2 + valor3**2
print(total)
"""

#----------------------------------------------------------
# EXERCÍCIO SEÇÃO 4 - Estruturas Lógicas e Condicionais
#----------------------------------------------------------

# 1
numero = int(input("Digite o primeiro numero inteiro: "))
numero2 = int(input("Digite o segundo numero inteiro: "))

if numero > numero2:
    print(f"{numero} é maior que {numero2}")
elif numero < numero2:
    print(f"{numero2} é maior que {numero}")
else:
    print("Escreva dois números inteiros distintos")

# 2

inteiro = int(input("Digite um numero inteiro: "))

if inteiro > 0:
    raiz = inteiro**(1/2)
    print(f"{raiz}")
elif inteiro < 0:
    print("Numero inválido")
else:
    print("Digite um numero diferente de zero")

# 3

num = int(input("Digite um numero inteiro: "))

if num % 2 == 0:
    print(f"{num} é um numero par")
else:
    print(f"{num} é um numero impar")

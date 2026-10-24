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
"""

#----------------------------------------------------------
# EXERCÍCIO SEÇÃO 5 - Estruturas de Repetição
#----------------------------------------------------------

"""
# 1
for numero in range(1, 18):
    if numero % 3 == 0:
        print(numero)


# 2

numero = 10

while numero >= 0:
    print(numero)
    numero = numero - 1

print("FIM!")


contador = valor_inicial

while condição:
    print(contador)
    contador = contador - 1


# 3

for numero in range(0, 101000, 1000):
    print(numero)
"""

# ---------------------------------------------------------
#             EXERCÍCIOS SOBRE LISTAS
# ---------------------------------------------------------

# 01
frutas = ["maçã", "banana", "laranja", "uva", "morango"]

print(frutas[0])
print(frutas[-1])

frutas[2] = "abacaxi"
print(frutas)

# 02
compras = []
compras.extend(['arroz', 'feijão', 'macarrão'])
compras.insert(1, 'leite')
compras.pop(2)
print(compras)
print(len(compras))

# 03

numeros = [10, 20, 30, 40, 50, 60]

for numero in numeros:
    quadrado = numero ** 2
    print(quadrado)

# 04

lista = [12, 43, 24, 65, 64, 66]
print(max(lista))
print(min(lista))

soma = 0
for elemento in lista:
    print(elemento)
    soma = soma + elemento
print(soma)

# OU
print(sum(lista))

# 05 - desafio

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

# 06

compras = []
'''
for i in range(5):
    pedido = input("Qual seu pedido? ")
    compras.append(pedido)

print("\nSua lista final de compras:")
print(compras)
'''
print()
print()
print()

# -------------------------------------------------
#            EXERCÍCIOS SOBRE TUPLAS
# -------------------------------------------------

# 01
meses_do_ano = (
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
)
# numero = int(input("Digite um número de 1 a 12 para ver o mês: "))

if 1 <= numero <= 12:
    mes_escolhido = meses_do_ano[numero - 1]
    print(f"O mês correspondente é: {mes_escolhido}")
else:
    print("Número inválido! Por favor, digite entre 1 e 12.")

# 02

alunos = [
    ("Ana", 8.5),
    ("Bruno", 7.0),
    ("Carlos", 9.2),
    ("Diana", 6.5)
]

soma_notas = 0
for aluno in alunos:
    soma_notas += aluno[1]

media_turma = soma_notas / len(alunos)
print(f"Média da turma: {media_turma:.2f}")

aluno_maior_nota = alunos[0][0]
maior_nota = alunos[0][1]

for aluno in alunos:
    nome = aluno[0]
    nota = aluno[1]

    if nota > maior_nota:
        maior_nota = nota
        aluno_maior_nota = nome

print(f"O(a) aluno(a) com a maior nota foi {aluno_maior_nota}, tirando {maior_nota}.")

# 03

dia_da_semana = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo')

numero = int(input("Digite um número de 1 a 7:"))
if numero < 7:
    dia_escolhido = dia_da_semana[numero - 1]
    print(dia_escolhido[numero])
elif numero == 7:
    dia_escolhido = dia_da_semana[numero - 1]
    print(dia_escolhido[numero])
else:
    numero = int(input("Digite um número de 1 a 7:"))


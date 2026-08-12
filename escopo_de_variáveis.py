"""
ESCOPO DE VARIÁVEIS

Podemos pensar principalmente em dois tipos de escopo:

1 - Variáveis globais:
    Variáveis globais são reconhecidas em várias partes do programa.
    Elas são declaradas fora de funções.

2 - Variáveis locais:
    Variáveis locais existem dentro do escopo em que foram criadas,
    principalmente dentro de funções.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel


TIPAGEM DINÂMICA

Python é uma linguagem de tipagem dinâmica. Isso significa que,
ao declararmos uma variável, nós não precisamos informar explicitamente
o tipo de dado dela.

O tipo é inferido a partir do valor atribuído à variável.

Exemplo em C:

int numero = 42;

Exemplo em Java:

int numero = 42;

Em Python:

numero = 42
"""


# --------------------------------------------------
# EXEMPLO 1 - Tipagem dinâmica
# --------------------------------------------------

numero = 42

print(numero)
print(type(numero))

# A mesma variável pode receber outro tipo de dado:
numero = 'Geek'

print(numero)
print(type(numero))


# --------------------------------------------------
# EXEMPLO 2 - Criando outra variável
# --------------------------------------------------

nao_existo = 'Oi'

print(nao_existo)


# --------------------------------------------------
# EXEMPLO 3 - Variável dentro de um if
# --------------------------------------------------

numero = 42

if numero > 10:
    novo = numero + 10
    print(novo)

print(novo) #FUNCIONA


numero = 6

if numero > 10:
    novo = numero + 10
    print(novo)

print(novo) #NÃO FUNCIONA

# Diferentemente de algumas linguagens, if, for e while não criam um novo escopo de variável em Python.
# Só criaria um novo escopo se a condição não for estabelecida.


# --------------------------------------------------
# EXEMPLO 4 - Variável dentro de uma função
# --------------------------------------------------

numero = 42  # variável global


def calcular():
    novo = numero + 10  # variável local
    print(novo)


calcular()

print(numero)  # funciona
print(novo)    # ERRO

# --------------------------------------------------
# EXEMPLO 5 - Se uma função precisar alterar uma variável global,
# existe a palavra-chave global
# --------------------------------------------------

numero = 42


def alterar_numero():
    global numero
    numero = 100


alterar_numero()  # <- EXECUTA a função

print(numero)

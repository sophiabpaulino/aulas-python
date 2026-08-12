"""
TIPO FLOAT

Float representa números reais/decimais.

Exemplos:
1.44
10.5
-3.7
0.25

IMPORTANTE:
Na programação, o separador das casas decimais é o PONTO (.)
e não a vírgula (,).
"""


# ============================================================
# FLOAT E VÍRGULA
# ============================================================

# Errado do ponto de vista de um número float.
# O Python interpreta isso como uma TUPLA contendo dois valores.

valor = 1, 44 #errado

print(valor)
print(type(valor))

# Resultado:
# (1, 44)
# <class 'tuple'>


# ============================================================
# CRIANDO UM FLOAT
# ============================================================

# Forma correta de representar um número decimal:

valor = 1.44

print(valor)
print(type(valor))

# Resultado:
# 1.44
# <class 'float'>


# ============================================================
# DUPLA ATRIBUIÇÃO
# ============================================================

# É possível atribuir valores para mais de uma variável
# na mesma linha.

valor1, valor2 = 1, 44

print(valor1)
print(type(valor1))

print(valor2)
print(type(valor2))

# Nesse caso:
# valor1 é int
# valor2 é int


# Outro exemplo:

numero1, numero2 = 10.5, 20.8

print(numero1)
print(numero2)

# Ambos são float.


# ============================================================
# CONVERSÃO DE FLOAT PARA INT
# ============================================================

"""
Podemos converter um float para um int usando int().

IMPORTANTE:
Ao converter um float para inteiro, perdemos a parte decimal.

O Python NÃO arredonda automaticamente.
Ele simplesmente remove a parte decimal.
"""

valor = 1.44

res = int(valor)

print(res)
print(type(res))

# Resultado:
# 1
# <class 'int'>


# Outro exemplo:

numero = 9.99

print(int(numero))

# Resultado:
# 9


# ============================================================
# CONVERSÃO DE INT PARA FLOAT
# ============================================================

numero = 10

numero_float = float(numero)

print(numero_float)
print(type(numero_float))

# Resultado:
# 10.0
# <class 'float'>


# ============================================================
# NÚMEROS COMPLEXOS
# ============================================================

"""
Python também possui números complexos.

A parte imaginária é representada pela letra j.
"""

variavel = 5j

print(variavel)
print(type(variavel))

# Resultado:
# 5j
# <class 'complex'>


numero_complexo = 3 + 5j

print(numero_complexo)
print(type(numero_complexo))


# ============================================================
# OBSERVAÇÃO IMPORTANTE SOBRE FLOAT
# ============================================================

"""
Computadores representam números float em formato binário.

Por isso, algumas operações podem apresentar pequenas
imprecisões.

Exemplo:
"""

print(0.1 + 0.2)

# Pode resultar em:
# 0.30000000000000004

# Para a maioria dos programas isso não é um problema.
# Porém, para cálculos financeiros que exigem precisão,
# normalmente é melhor utilizar Decimal.
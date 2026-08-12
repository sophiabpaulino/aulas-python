"""
TIPO BOOLEANO (bool)

O tipo booleano trabalha com apenas dois valores:

True  -> Verdadeiro
False -> Falso

A lógica booleana tem origem na Álgebra Booleana,
desenvolvida por George Boole.

IMPORTANTE:
True e False devem começar com letra MAIÚSCULA.

Errado:
true
false

Certo:
True
False
"""


# ============================================================
# CRIANDO UM BOOLEANO
# ============================================================

ativo = False

print(ativo)
print(type(ativo))

# Resultado:
# False
# <class 'bool'>


# ============================================================
# OPERAÇÕES BOOLEANAS
# ============================================================

# NOT - NEGAÇÃO


"""
O operador not inverte um valor booleano.

True  -> False
False -> True
"""

ativo = False

print(not ativo)

# Como ativo é False:
# not False -> True


ativo = True

print(not ativo)

# not True -> False


# OR - OU


"""
O operador or depende de dois valores.

Para o resultado ser True, pelo menos UM dos valores
precisa ser verdadeiro.

Tabela verdade:

True  or True  -> True
True  or False -> True
False or True  -> True
False or False -> False
"""

ativo = False
logado = False

print(ativo or logado)


# Outro exemplo:

ativo = True
logado = False

print(ativo or logado)

# Resultado:
# True


# AND - E


"""
O operador and também depende de dois valores.

Para o resultado ser True, AMBOS os valores precisam
ser verdadeiros.

Tabela verdade:

True  and True  -> True
True  and False -> False
False and True  -> False
False and False -> False
"""

ativo = True
logado = True

print(ativo and logado)

# Resultado:
# True


ativo = True
logado = False

print(ativo and logado)

# Resultado:
# False


# ============================================================
# BOOLEANOS EM COMPARAÇÕES
# ============================================================

"""
Comparações normalmente produzem valores booleanos.
"""

idade = 20

print(idade >= 18)
# True

print(idade < 18)
# False

print(10 == 10)
# True

print(10 != 5)
# True


# ============================================================
# OPERADORES DE COMPARAÇÃO
# ============================================================

"""
==   igual
!=   diferente
>    maior
<    menor
>=   maior ou igual
<=   menor ou igual
"""


# ============================================================
# EXEMPLO PRÁTICO
# ============================================================

idade = 20
tem_carteira = True

pode_dirigir = idade >= 18 and tem_carteira

print(pode_dirigir)

# True


# ============================================================
# OBSERVAÇÃO IMPORTANTE
# ============================================================

"""
Não confunda:

=   atribuição
==  comparação

Exemplo:

idade = 20
    Coloca o valor 20 na variável idade.

idade == 20
    Pergunta se idade é igual a 20.
    O resultado será True ou False.
"""
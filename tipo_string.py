"""
TIPO STRING (str)

Strings representam textos.

Em Python, um dado é considerado string quando estiver
entre aspas.

Podemos utilizar:

'aspas simples'

"aspas duplas"

'''aspas simples triplas'''

\"""aspas duplas triplas\"""


"""

# ============================================================
# CRIANDO STRINGS
# ============================================================

nome = 'Geek University'

print(nome)
print(type(nome))

# Resultado:
# Geek University
# <class 'str'>


# ============================================================
# ASPAS DENTRO DE STRINGS
# ============================================================

# Podemos utilizar aspas duplas por fora quando precisamos
# utilizar uma aspa simples dentro do texto.

nome = "Gina's Bar"

print(nome)
print(type(nome))


# ============================================================
# \n - QUEBRA DE LINHA
# ============================================================

nome = 'Angelina \nJolie'

print(nome)
print(type(nome))

# Resultado:
# Angelina
# Jolie


# ============================================================
# CARACTERE DE ESCAPE \
# ============================================================

"""
A barra invertida \ é utilizada como caractere de escape.

Ela permite que determinados caracteres sejam tratados
como parte da string.
"""

nome = "Angelina \" Jolie"

print(nome)
print(type(nome))


# ============================================================
# UPPER
# ============================================================

# upper() transforma as letras em maiúsculas.

nome = 'Geek University'

print(nome.upper())

# Resultado:
# GEEK UNIVERSITY


# ============================================================
# LOWER
# ============================================================

# lower() transforma as letras em minúsculas.

print(nome.lower())

# Resultado:
# geek university


# ============================================================
# SPLIT
# ============================================================

"""
split() divide uma string.

Por padrão, a divisão acontece nos espaços.

O resultado é uma LISTA.
"""

nome = 'Geek University'

print(nome.split())

# Resultado:
# ['Geek', 'University']


# Podemos acessar cada parte:

print(nome.split()[0])

# Geek


print(nome.split()[1])

# University


# ============================================================
# ÍNDICES DE UMA STRING
# ============================================================

"""
Cada caractere possui uma posição (índice).

Exemplo:

nome = 'Geek University'

Índices:

 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14
 G  e  e  k     U  n  i  v  e  r  s  i  t  y

IMPORTANTE:
Os índices começam em ZERO.
"""

nome = 'Geek University'


# ============================================================
# SLICE DE STRING
# ============================================================

"""
Slice permite pegar apenas uma parte da string.

Sintaxe:

string[inicio:fim]

IMPORTANTE:
O índice inicial é incluído.
O índice final NÃO é incluído.
"""

print(nome[0:4])

# Resultado:
# Geek


print(nome[5:15])

# Resultado:
# University


# ============================================================
# INVERTENDO UMA STRING
# ============================================================

"""
Sintaxe:

[::-1]

Significa percorrer a string utilizando passo -1,
ou seja, de trás para frente.
"""

nome = 'Geek University'

print(nome[::-1])

# Resultado:
# ytisrevinU keeG


# ============================================================
# REPLACE
# ============================================================

"""
replace() substitui uma parte da string por outra.

Sintaxe:

string.replace('antigo', 'novo')
"""

print(nome.replace('e', 'i'))

# Resultado:
# Giik Univirsity


print(type(nome))

# <class 'str'>


# ============================================================
# PALÍNDROMOS
# ============================================================

"""
Um palíndromo é uma palavra ou frase que pode ser lida
da mesma maneira de frente para trás e de trás para frente.

Exemplo simples:

ana
"""

nome = 'ana'

print(nome)
print(nome[::-1])

# Os dois resultados serão:
# ana


# Exemplo com uma frase:

texto = 'socorram me subino onibus em marrocos'

print(texto)
print(texto[::-1])


# ============================================================
# TAMANHO DE UMA STRING
# ============================================================

# len() informa quantos caracteres existem.

nome = 'Geek University'

print(len(nome))

# O espaço também é contado como caractere.


# ============================================================
# ACESSANDO CARACTERES
# ============================================================

nome = 'Python'

print(nome[0])
# P

print(nome[1])
# y

print(nome[-1])
# n

"""
Índices negativos começam pelo final:

-1 -> último caractere
-2 -> penúltimo
-3 -> antepenúltimo
"""


# ============================================================
# STRINGS SÃO IMUTÁVEIS
# ============================================================

"""
Uma característica MUITO importante do Python:

Strings são imutáveis.

Isso significa que não podemos alterar diretamente
um caractere de uma string.

Por exemplo, isto gera erro:

nome = 'Python'
nome[0] = 'J'

Se quisermos uma string diferente, precisamos criar
uma nova string.
"""


# ============================================================
# F-STRINGS
# ============================================================

"""
Uma maneira moderna e muito utilizada de colocar variáveis
dentro de textos são as f-strings.
"""

nome = 'Ana'
idade = 20

print(f'Meu nome é {nome} e tenho {idade} anos.')


# ============================================================
# OUTROS MÉTODOS ÚTEIS
# ============================================================

texto = '   Python é muito legal   '

# Remove espaços no começo e no final:
print(texto.strip())

# Verifica se começa com determinado texto:
print(texto.strip().startswith('Python'))

# Verifica se termina com determinado texto:
print(texto.strip().endswith('legal'))

# Conta quantas vezes algo aparece:
palavra = 'banana'

print(palavra.count('a'))

# Resultado:
# 3
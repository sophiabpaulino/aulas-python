"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas. Existem, basicamente, duas diferenças:

1 - As tuplas são representadas por ();
2 - As tuplas são imutáveis: Ao se criar uma tupla ela não muda. Toda
operação em uma tupla gera uma nova tupla.

"""
# OBSERVAÇÃO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5)
print(tupla1)
print(type(tupla1))
tupla2 = 1, 2, 3, 4, 5 # Ou seja, as tuplas são REPRESENTADAS por (), mas podem ser criadas com ou sem ().
print(tupla2)
print(type(tupla2))

# OBSERVAÇÃO 2: Tuplas com apenas 1 elemento

tupla3 = (3) # Isso não é uma tupla! Python consta como INT
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # Isso é uma tupla!
print(tupla4)
print(type(tupla4)) # Ou seja, as tuplas são DEFINIDAS pela vírgula e não pelo ().

# Podemos gerar uma tupla com range(ínicio, fim, passo):

tupla5 = tuple(range(5))
print(tupla5)
print(type(tupla5))

# Desempacotamento de Tupla

tupla = ('Sophia', 'Paulino')
nome, sobrenome = tupla
print(nome)
print(sobrenome) # OBS: gera erro (ValueError) se colocarem um número diferente
# de elementos para desempacotar.

# Métodos para: adição, remoção de elementos nas tuplas não existem, dado o fato delas
# serem imutáveis.

# Soma*, Valor Mínimo*, Valor máximo* e Tamanho (* = somente se os valores forem inteiros ou reais)

tupla6 = (1, 2, 3, 5, 7, 4, 2) # -> se colocar string, os 3 primeiros dão erro.
print(sum(tupla6))
print(max(tupla6))
print(min(tupla6))
print(len(tupla6))

# Concatenação de tuplas

print(tupla6 + tupla5)
# Elas são se alteram. Apenas se juntam.

tupla4 = tupla4 + tupla1
print(tupla4) # São imutáveis, mas podemos sobrescrever seus valores.

# Verificar se determinado elemento está contido na tupla

tuple_1 = (1, 2, 4)
print(2 in tuple_1)

# Iterando sobre uma tupla

tupla_2 = (1, 2, 4, 6)
for n in tupla_2:
    print(n)

for indice, valor in enumerate(tupla_2):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla_3 = ('a', 'b', 'c', 'd', 'e', 'a', 'v', 'b', 'b')
print(tupla_3.count('a'))

curso = tuple('ciência da computação')
print(curso)
print(curso.count('c'))

"""
Dicas na utilização de TUPLAS:
1 - Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados 
contidos em um coleção
2 - Acesso a elemtnos de um tupla é semelhante a de uma lista
3 - Iterar com While
4 - Verificar em qual índice um elemento está na tupla
5 - Slicing -> tupla[inicio:fim:passo]
"""
# Exemplo 1

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho')

# Exemplo 2

print(meses[5])

# Exemplo 3
i = 0
while i < len(meses):
    print(meses[i])
    i += 1

# Exemplo 4

print(meses.index('fevereiro')) # Caso o elemento não esteja na tupla, será gerado ValueError

# Exemplo 5

print(meses[5:7])

"""
Por que utilizar tuplas?

- Tuplas são mais rápidas do que listas;
- Elas deixam seu código mais "seguro" -> trabalhar com elementos
imutáveis traz segurança para o código

"""

# Copiando uma Tupla para outra

antiga = (1, 'b', 9, 8)
print(antiga)

nova = antiga # Na tupla não temos o problema de shallow copy
print(nova)

outra = (4, 5, 6)
nova = nova + outra
print(nova)
print(antiga)




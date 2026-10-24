"""
Listas

Listas em python funcionam como vetores/matrizes (arrays= em outras linguagens), com a diferença
de serem DINÂMICOS e, também, poderem colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
- Possuem tamanho e tipo de dado fixo, ou seja nestas linguagens se você criar um array do tipo int
e com tamanho 5, este array será SEMPRE do tipo int e poderá ter sempre, no máximo, 5 valores.

Já em PYTHON:
- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos.
- Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado.
- Listas aceitam valores repetidos.

As listas em PYTHON são representadas por colchetes: []


"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek university')
lista6 = ['amigo', 'frederico', 'amaro', 'amparo', 'marrie', 'friends', 'Jesus', 'gustavo', 'america', 'marrie', 'jonas', 'barco', 'marrie', 'lucasa', 'avante', 'marrie' ]

#Podemos realmente colocar qualquer tipo de dados em uma lista, inclusive misturando esses dados.
lista10 = ['apolo', 1, 2.43, True, [1, 2, 3, 4], 22333344354546545, 'p', 'overwacth', 6, 7]


# Podemos facilmente checar se determinado valor está contido na lista
num = 14
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Nao encontrei numero {num}')

if 'e' in lista5:
    print('Encontrei a letra E')
else:
    print('Nao encontrei a letra E')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))
print(lista6.count('marrie'))

# Adicionar elementos em listas
"""
Para adicionar elementos e valores em listas, utilizamos a função .append()
"""
print(lista1)
lista1.append(50)
print(lista1)

# OBS: com .append(), nós só conseguimos adicionar 1 elemento por vez.
#lista1.append(50, 24, 25, 32) -> ERRO

lista1.append([1, 2, 4, 6, 4]) # Coloca a lista como elemento único (subslista).
print(lista1)

if [1, 2, 4, 6, 4] in lista1:
    print('Encontrei a lista')
else:
    print('Nao encontrei a lista')

lista1.extend([32, 21, 67]) # Coloca cada elemento da lista como valor adicional a lista.
print(lista1)
# O extend só aceita os elementos iteráveis (lista, srting)
# O append e o extend sempre adicionam o elemento no final da lista.

# Podemos inserir novo elemento na lista informando a posição do índice
lista1.insert(2, 'Novo Valor')
print(lista1)
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.

# Podemos facilmente juntar duas listas:

#FORMA 1
lista7 = lista1 + lista2
print(lista7)

#FORMA 2
lista1.extend(lista2)
print(lista1)

#FORMA 3
lista1 = lista1 + lista2
print(lista1)

print()
# Podemos facilmente inverter uma lista
#FORMA 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

#FORMA 2
print(lista1[::-1])
print(lista2[::-1])

# Podemos facilmente copiar uma lista
lista8 = lista5.copy()
print(lista8)

# Podemos contar quantos elementos existem na lista

print(len(lista8))

# Podemos remover facilmente o último elemento de uma lista

lista5.pop() # Remove o elemento, mas também retorna o mesmo
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: os elementos a direita deste índice serão deslocados para a esquerda
# se não houver elemento no índice informado, teremos o erro IndexError
lista1.pop(2)
print(lista1)

# Podemos remover todos os elementos (zerar a lista)
lista4.clear()
print(lista4)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 4, 5]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma srting para uma lista

# EXEMPLO 1

curso = 'Programação em python: essencial'
print(curso)
curso = curso.split()
print(curso)

#OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas

# EXEMPLO 2

cursar = 'programação,em,python,essencial'
print(cursar)
cursar = cursar.split(',')
print(cursar)

# Convertendo uma lista em uma string

minha_lista = ['Sophia', 'Borges', 'Paulino']
print(minha_lista)
minha_lista = ' '.join(minha_lista) # Pega a minha_lista, coloca espaço entre cada elemento e transforme em uma string
print(minha_lista)

# Iterando sobre listas

# EXEMPLO 1 - Utilizando for
list = [1, 2, 3, 4, 5, 7]

soma = 0
for elemento in list:
    print(elemento)
    soma = soma + elemento #somar os elementos da lista
print(soma)

# EXEMPLO 2 - Utilizando while

carrinho = [ ]
produto = ' '

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas

numeros = [1, 2, 3, 4, 5, 6]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
num6 = 6

numeros = [num1, num2, num3, num4, num5, num6]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0]) #verde
print(cores[1]) #amarelo
print(cores[2]) #azul
print(cores[3]) #branco

# Fazer acesso aos elementos de forma indexada inversa

print(cores[-1]) #branco
print(cores[-2]) #azul
print(cores[-3]) #amarelo
print(cores[-4]) #verde
# print(cores[-5]) -> Erro, pois não existe índice -5

print()
for cor in cores:
    print(cor)

print()
# Enquanto o índice for menor que 4 (número de elemento da lista cores) imprima as cores na posição índice
indice = 0
while indice < len(cores): #len é tamanho, tamanho da lista
    print(cores[indice])
    indice = indice + 1

# Gerar índice em um for

#   chave  valor
for indice, cor in enumerate(cores):
    print(indice, cor)

# Subsitutir um elemento por outro elemento em uma lista

frutinhas = ["maçã", "banana", "laranja", "uva", "morango"]

# FORMA 01
frutinhas[2] = ("abacaxi")
print(frutinhas)

# FORMA 02
indice = frutinhas.index("laranja")
frutinhas[indice] = "abacaxi"
print(frutinhas)

"""
Outros métodos não tao importantes, mas úteis.
"""
# Encontrar o índice de um elemento na lista

numbers = [5, 6, 7, 8, 9, 5, 8, 10]
print(numbers.index(6)) # Em qual índice da lista está o valor 6?
print(numbers.index(9)) # Em qual índice da lista está o valor 9?
# print(numbers.index(19)) - OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError
print(numbers.index(8)) # Retorna o índice do primeiro elemento encontrado

# Podemos fazer busca dentro de um range, ou seja, qual ìndice começar a buscar
print(numbers.index(5, 1)) # buscando a partir do índice 1.
# print(numbers.index(6,3) -> caso não tenha na lista, será apresentado erro

# Podemos fazer busca dentro de um range, inicio/fim
print(numbers.index(8, 1, 5)) # buscar o índice do valor 8, entre os índices 1 a 5.



# Revisão de Slicing -> lista[inicio:fim:passo]  ou  range(inicio:fim:passo)
# Trabalhando com slice de lista com o parâmetro 'ínicio'

revisao = [1, 2, 3, 4]
print(revisao[1:]) # iniciando o índice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parâmetro 'fim'

print(revisao[:2]) # começa em 0, pega até o índice 2 - 1.

print(revisao[:4]) # começa em 0, pega até o índice 4 - 1.

print(revisao[1:3]) # começa em 1, pega até o índice 3 - 1.

# Trabalhando com o slice de lista com o parâmetro 'passo'

print(revisao[1::2]) # começa em 1, vai até o final de 2 em 2.

print(revisao[::2])  # começa em 0, vai até o final de 2 em 2.

print(revisao[1::-1]) # começa do 1, vai até o final, invertendo a lista.

# práticar slicing na hora dos exercícios

# Invertendo valores em uma lista

inverter = ['Marrie', 'Curie']

#FORMA 1
inverter[0], inverter[1] = inverter[1], inverter[0]
print(inverter)

# FORMA 2
inverter.reverse()
print(inverter)

# ------------------- IMPORTANTE! -----------------------------
# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho de uma lista.
# * APENAS SE TODOS OS VALORES FOREM INTEIROS OU REAIS.

values = [1, 2, 4, 5, 7, 9, 12]

print(sum(values)) # soma
print(max(values)) # máximo valor
print(min(values)) # mínimo valor
print(len(values)) # tamanho

# Transformar uma lista em tupla

print(values)
print(type(values))
tupla = tuple(values)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

desempacotamento = [1, 2, 3]

num1, num2, num3 = desempacotamento

print(num1, num2, num3)
print()
print(num1)
print(num2)
print(num3)
# - OBS: Se tivermos um número diferente de elementos na lista ou variáveis para receber os dados, teremos erro.

# Copiando uma lista para outra (Shallow copy e Deep Copy)

# FORMA 1 - DEEP COPY

lista_original = ['a', 'b', 'c']
print(lista_original)

nova = lista_original.copy() # cópia
print(nova)
nova.append(4)
print(nova)
'''
 - Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
ficaram totalmente independentes, ou seja, modificando uma lista não afeta a outra. Isso em python é
chamado de Deep Copy (cópia profunda);
'''

# FORMA 2 - SHALLOW COPY

before = [1, 2, 3]
print(before)

after = before
print(after)

after.append(4)
print(before)
print(after)
'''
- Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
após realizar modificação em uma das listas, essa modificação se refletiu em AMBAS as listas
isso em PYTHON é: SHALLOW COPY
'''
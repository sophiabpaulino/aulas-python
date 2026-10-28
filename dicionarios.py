"""
Dicionários (Em algumas linguagens de programação, os dicionários
python são conhecidos por mapas.

- são coleções do tipo chave/valor.
- são representados por chaves {}
- Chave e valor são separados por dois pontos :
- Tanto chave quanto valor podem ser de qualquer tipo de dado (listas, tuplas
dicionários, int, float, string, boolean)
- Podemos misturar tipos de dados

"""
# CRIAÇÃO DE DICIONÁRIOS

# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'esp': 'Espanha'}
print(paises)
print(type(paises))

# Forma 2 (Menos Comum)
paises2 = dict(br='Brasil', eua='Estados Unidos', esp='Espanha')
print(paises2)
print(type(paises2))

# ACESSANDO ELEMENTOS

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['eua'])
# print(paises['arg']) Caso tente fazer o acesso utilizando uma chave que não
# existe, teremos KeyError

# Forma 2 - Acessando via get (recomendado)
print(paises.get('br'))
print(paises.get('eua'))
print(paises.get('arg')) # Quando o elemento não se encontra no dicionário
# o get retorna None, ao invés de KeyError

print(paises.get('ale', 'Não encontrado')) # procure a chave 'ale', caso não encontre,
# imprima 'não encontrado'. (valor padrão)

# VERIFICAR SE TAL CHAVE SE ENCONTRA NO DICIONÁRIO

print('br' in paises) # -> TRUE
print('arg' in paises) # -> FALSE
print('Brasil' in paises) # -> FALSE, é um valor e não uma chave

# TUPLAS DENTRO DE UM DICIONÁRIO
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))

# ADICIONAR ELEMENTOS EM UM DICIONÁRIO

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado)  # receita.update({'mai': 500})

print(receita)
# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas.

# REMOVER DADOS DE UM DICIONÁRIO

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1
ret = receita.pop('mar')
print(ret)
print(receita)
# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2
del receita['fev']
print(receita)

# Se a chave não existir será gerado um KeyError
# OBS: Neste caso o valor removido não é retornado.

"""
Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.
Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;
"""
# 1 - Poderíamos utilizar uma Lista para isso? Sim

carrinho = []

produto1 = ['Paystation 4', 1, 230.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
# Teríamos que saber qual é o índice de cada informação no produto.

# 2 - Poderíamos utilizar uma Tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# 3 - Poderíamos utilizar um Dicionário para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação.

# MÉTODOS DE DICIONÁRIOS

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário (Zerar dados)
d.clear()
print(d)

# Copiando um dicionário para outro

# Forma 1 # Deep Copy

novo = d.copy()
print(novo)
novo['d'] = 4

print(d)
print(novo)

# Forma 2 # Shallow Copy

novo = d

print(novo)
novo['d'] = 4
print(d)
print(novo)


# FORMA NÃO USUAL DE CRIAÇÃO DE DICIONÁRIOS

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O uso de .fromkeys recebe dois parâmetros: um iterável e um valor
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)


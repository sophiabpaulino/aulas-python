"""
=========================================================
LOOP FOR EM PYTHON
=========================================================

O for é uma estrutura de repetição.

Mas atenção:

O for NÃO precisa do range() para funcionar.

A estrutura básica do for é:

for elemento in iteravel:
    # código que será repetido


A ideia é:

"Para cada elemento que existir dentro desse iterável,
execute determinado código."


---------------------------------------------------------
O QUE É UM ITERÁVEL?
---------------------------------------------------------

Um iterável é, de forma simplificada, alguma coisa que o Python
consegue percorrer elemento por elemento.

Exemplos:


String:
    nome = "Maria"


Lista:
    numeros = [10, 20, 30]


Range:
    range(1, 5)


Tupla:
    cores = ("azul", "verde", "rosa")


Portanto:

for NÃO significa "usar range".

O for percorre ITERÁVEIS.

O range() é apenas uma das coisas que podemos entregar para o for.
"""


# =========================================================
# EXEMPLO 1 - FOR COM UMA STRING
# =========================================================

nome = "Ana"

for letra in nome:
    print(letra)

"""
O Python percorre a string letra por letra.

1ª repetição:
letra = "A"

2ª repetição:
letra = "n"

3ª repetição:
letra = "a"

Resultado:

A
n
a
"""


# =========================================================
# EXEMPLO 2 - FOR COM UMA LISTA
# =========================================================

frutas = ["maçã", "banana", "uva"]

for fruta in frutas:
    print(fruta)

"""
Aqui também NÃO precisamos de range().

O Python faz aproximadamente:

1ª repetição:
fruta = "maçã"

2ª repetição:
fruta = "banana"

3ª repetição:
fruta = "uva"

Depois que não existem mais elementos na lista,
o for termina.
"""


# =========================================================
# EXEMPLO 3 - FOR COM RANGE
# =========================================================

for numero in range(1, 5):
    print(numero)

"""
Resultado:

1
2
3
4

Nesse caso usamos range() porque queríamos gerar
uma sequência de números.

IMPORTANTE:

range(1, 5)

gera:

1, 2, 3, 4

O número 5 NÃO entra.


Portanto, pense assim:

FOR:
    percorre alguma coisa.

RANGE:
    gera uma sequência de números.

Então:

for + range

é muito comum, mas o range NÃO é obrigatório.
"""


# =========================================================
# RANGE PARA REPETIR ALGO UMA QUANTIDADE DE VEZES
# =========================================================

for numero in range(3):
    print("Olá!")

"""
Resultado:

Olá!
Olá!
Olá!

range(3) gera:

0, 1, 2

Ou seja, existem 3 valores e, consequentemente,
o for executa 3 vezes.
"""


# =========================================================
# ENUMERATE
# =========================================================

"""
Agora vamos entender o enumerate().

Imagine esta lista:

frutas = ["maçã", "banana", "uva"]

Se fizermos:

for fruta in frutas:
    print(fruta)

conseguimos acessar cada fruta.

Mas e se quisermos saber também a POSIÇÃO de cada fruta?

Por exemplo:

0 -> maçã
1 -> banana
2 -> uva

É justamente aí que enumerate() é muito útil.


O enumerate() nos permite obter:

ÍNDICE + VALOR

ao mesmo tempo.
"""


frutas = ["maçã", "banana", "uva"]

for indice, fruta in enumerate(frutas):
    print(indice, fruta)

"""
Resultado:

0 maçã
1 banana
2 uva


Podemos imaginar o enumerate() produzindo pares:

(0, "maçã")
(1, "banana")
(2, "uva")


Então nesta linha:

for indice, fruta in enumerate(frutas):

o Python vai fazer aproximadamente:


PRIMEIRA REPETIÇÃO:

indice = 0
fruta = "maçã"


SEGUNDA REPETIÇÃO:

indice = 1
fruta = "banana"


TERCEIRA REPETIÇÃO:

indice = 2
fruta = "uva"
"""


# =========================================================
# PARA QUE USAMOS ENUMERATE?
# =========================================================

"""
Usamos enumerate() principalmente quando precisamos
do VALOR e também da POSIÇÃO desse valor.

Exemplo:

Queremos mostrar uma lista numerada de alunos.
"""

alunos = ["Ana", "Carlos", "Pedro"]

for indice, aluno in enumerate(alunos):
    print(indice, aluno)

"""
Resultado:

0 Ana
1 Carlos
2 Pedro
"""


# =========================================================
# FAZENDO A CONTAGEM COMEÇAR EM 1
# =========================================================

"""
Normalmente os índices começam em 0.

Mas podemos pedir para enumerate() começar em 1.
"""

alunos = ["Ana", "Carlos", "Pedro"]

for numero, aluno in enumerate(alunos, start=1):
    print(numero, aluno)

"""
Resultado:

1 Ana
2 Carlos
3 Pedro

Isso é muito útil para:

- listas numeradas
- menus
- rankings
- perguntas
- cadastro de pessoas
- mostrar posições para o usuário
"""


# =========================================================
# EXEMPLO PRÁTICO
# =========================================================

materias = ["Python", "Banco de Dados", "Algoritmos"]

for numero, materia in enumerate(materias, start=1):
    print(f"{numero} - {materia}")

"""
Resultado:

1 - Python
2 - Banco de Dados
3 - Algoritmos
"""


# =========================================================
# ENTENDENDO MELHOR O ENUMERATE
# =========================================================

nome = "Ana"

for indice, letra in enumerate(nome):
    print(indice, letra)

"""
Resultado:

0 A
1 n
2 a

Ou seja, enumerate() também funciona com strings.

Temos:

índice 0 -> A
índice 1 -> n
índice 2 -> a
"""


# =========================================================
# USANDO O ÍNDICE PARA ACESSAR O ELEMENTO
# =========================================================

nome = "Ana"

for indice, letra in enumerate(nome):
    print(nome[indice])

"""
Resultado:

A
n
a


Mas perceba uma coisa:

O enumerate() já entregou a letra para nós na variável "letra".

Então fazer:

print(nome[indice])

funciona, mas neste caso é desnecessário.

Podemos simplesmente fazer:
"""

for indice, letra in enumerate(nome):
    print(letra)


# =========================================================
# E SE EU NÃO PRECISAR DO ÍNDICE?
# =========================================================

"""
Se não precisamos do índice, provavelmente nem precisamos
usar enumerate().

Podemos simplesmente fazer:
"""

for letra in nome:
    print(letra)


"""
Porém, às vezes usamos funções que retornam mais de um valor
e queremos ignorar um deles.

Por convenção, em Python usamos "_" para indicar:

"Estou recebendo esse valor, mas não vou utilizá-lo."
"""

for _, letra in enumerate(nome):
    print(letra)


# =========================================================
# ENUMERATE SEM SEPARAR OS VALORES
# =========================================================

"""
Também podemos escrever:
"""

for valor in enumerate(nome):
    print(valor)

"""
Nesse caso, em vez de separar índice e letra,
a variável "valor" recebe os dois juntos.

Resultado:

(0, 'A')
(1, 'n')
(2, 'a')


Esses valores entre parênteses são TUPLAS.

Portanto:

enumerate(nome)

produz algo semelhante a:

(0, 'A')
(1, 'n')
(2, 'a')


Quando escrevemos:

for indice, letra in enumerate(nome):

o Python separa automaticamente:

0 e 'A'
1 e 'n'
2 e 'a'

nas duas variáveis.
"""
# =========================================================
# ENTENDENDO O RANGE
# =========================================================

"""
Ranges são utilizados para gerar sequências numéricas.

Existem três formas principais de utilizar range():

1) range(parada)

2) range(inicio, parada)

3) range(inicio, parada, passo)

Também podemos utilizar um passo negativo para fazer
uma sequência decrescente.
"""


# =========================================================
# FORMA 1
# range(parada)
# =========================================================

"""
O início padrão é 0.
O passo padrão é 1.
O valor de parada NÃO é incluído.
"""

for num in range(11):
    print(num)

# Resultado:
# 0 1 2 3 4 5 6 7 8 9 10


# =========================================================
# FORMA 2
# range(inicio, parada)
# =========================================================

"""
Definimos onde o range começa.

O passo continua sendo 1 por padrão.
O valor de parada NÃO é incluído.
"""

for num in range(4, 11):
    print(num)

# Resultado:
# 4 5 6 7 8 9 10


# =========================================================
# FORMA 3
# range(inicio, parada, passo)
# =========================================================

"""
Aqui podemos definir:

- valor inicial
- valor de parada
- passo

O valor de parada continua NÃO sendo incluído.
"""

for num in range(5, 55, 5):
    print(num)

# Resultado:
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50


# =========================================================
# FORMA 4 - RANGE INVERSO
# =========================================================

"""
Para fazer uma contagem regressiva utilizamos um passo negativo.

range(inicio, parada, passo)
"""

for num in range(10, -1, -1):
    print(num)

# Resultado:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0


# =========================================================
# RESUMÃO MENTAL
# =========================================================

"""
Guarde estas três ideias:


1) FOR
---------------------------------------------------------

Percorre um iterável.

for elemento in iteravel:
    ...


Exemplo:

for fruta in frutas:
    print(fruta)



2) RANGE
---------------------------------------------------------

range(parada)

range(inicio, parada)

range(inicio, parada, passo)


Gera uma sequência de números.

range(1, 5)

gera:

1, 2, 3, 4


Podemos usar essa sequência dentro de um for:

for numero in range(1, 5):
    print(numero)



3) ENUMERATE
---------------------------------------------------------

Usamos quando queremos saber:

POSIÇÃO + VALOR

Exemplo:

frutas = ["maçã", "banana", "uva"]

for indice, fruta in enumerate(frutas):
    print(indice, fruta)


Resultado:

0 maçã
1 banana
2 uva


Podemos pensar assim:

for       -> "para cada coisa..."

range     -> "gere números..."

enumerate -> "me dê a posição e o valor..."





"""

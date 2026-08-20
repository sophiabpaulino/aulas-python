"""
=========================================================
LOOP WHILE
=========================================================

O while é uma estrutura de repetição.

"while" significa "enquanto".

A ideia é:

ENQUANTO uma determinada condição for verdadeira,
continue executando o código.


Forma geral:

while expressao_booleana:
    # código que será repetido


Exemplo:

while numero < 10:
    print(numero)


O bloco do while será repetido ENQUANTO:

numero < 10

for verdadeiro.


---------------------------------------------------------
O QUE É UMA EXPRESSÃO BOOLEANA?
---------------------------------------------------------

Uma expressão booleana é uma expressão cujo resultado
é True (verdadeiro) ou False (falso).

Exemplos:

5 < 10
Resultado: True

10 < 5
Resultado: False

5 == 5
Resultado: True

5 != 5
Resultado: False


Podemos testar isso no Python:

print(5 < 10)
print(10 < 5)

Resultado:

True
False
"""


# =========================================================
# EXEMPLO 1 - WHILE COM CONTADOR
# =========================================================

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1


"""
O que acontece aqui?

Começamos com:

numero = 1


Depois o Python pergunta:

numero < 10?

1 < 10 -> True

Então entra no while:

print(numero)

e depois:

numero = numero + 1


Agora:

numero = 2


O Python volta para o começo e pergunta novamente:

2 < 10?

True.

Então executa novamente.


Isso continua até:

numero = 10


Nesse momento:

10 < 10?

False.


Como a condição ficou False, o while termina.


Resultado:

1
2
3
4
5
6
7
8
9
"""


# =========================================================
# FORMA MAIS CURTA DE SOMAR 1
# =========================================================

"""
Em vez de:

numero = numero + 1

podemos escrever:

numero += 1


As duas formas fazem a mesma coisa.
"""

numero = 1

while numero < 10:
    print(numero)
    numero += 1


# =========================================================
# CUIDADO COM LOOP INFINITO
# =========================================================

"""
Em um loop while, é MUITO importante pensar:

"Em algum momento essa condição vai se tornar False?"


Por exemplo, isto seria perigoso:


numero = 1

while numero < 10:
    print(numero)


Perceba que "numero" nunca muda.

Ele começa sendo 1.

Então:

1 < 10 -> True

Depois:

1 < 10 -> True

Depois:

1 < 10 -> True

E assim por diante...


Isso cria um LOOP INFINITO.


Por isso normalmente precisamos de alguma coisa que altere
a condição do while.

Por exemplo:

numero += 1


Assim temos:

1
2
3
4
5
6
7
8
9

e eventualmente chegamos em 10.

Quando:

10 < 10

for False, o loop termina.


REGRA IMPORTANTE:

Ao criar um while, procure identificar o
CRITÉRIO DE PARADA.

Ou seja:

"O que fará esse while parar?"
"""


# =========================================================
# EXEMPLO 2 - WHILE COM RESPOSTA DO USUÁRIO
# =========================================================

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')


"""
Aqui não sabemos quantas vezes o usuário vai responder.

Por isso o while é muito útil.


Começamos com:

resposta = ''


Depois verificamos:

resposta != 'sim'


Isso significa:

"resposta é diferente de 'sim'?"


Como:

'' != 'sim'

é True, entramos no while.


Então perguntamos:

Já acabou Jéssica?


Se o usuário responder:

não

a condição continua:

'não' != 'sim'

True


Então o while pergunta novamente.


Se o usuário responder:

sim


teremos:

'sim' != 'sim'

False


O while termina.


Podemos ler o código quase como português:

ENQUANTO resposta for diferente de "sim":
    pergunte novamente.
"""


# =========================================================
# MELHORIA - ACEITANDO "SIM", "Sim", "sim"...
# =========================================================

"""
Um pequeno problema do exemplo anterior é que:

sim

e:

Sim

são strings diferentes para o Python.


Podemos utilizar .lower() para transformar a resposta
em letras minúsculas.
"""

resposta = ''

while resposta.lower() != 'sim':
    resposta = input('Já acabou Jéssica? ')


"""
Agora respostas como:

SIM
Sim
sIm
sim

serão transformadas em:

sim

antes da comparação.
"""


# =========================================================
# DIFERENÇA PRINCIPAL ENTRE FOR E WHILE
# =========================================================

"""
Uma forma simples de pensar:


FOR
---------------------------------------------------------

É muito utilizado quando queremos PERCORRER alguma coisa.

Exemplo:

for fruta in frutas:
    print(fruta)


Ou quando temos uma quantidade/sequência definida:

for numero in range(1, 6):
    print(numero)


Sabemos que teremos:

1
2
3
4
5


WHILE
---------------------------------------------------------

É muito útil quando queremos repetir algo ENQUANTO
uma condição continuar verdadeira.

Exemplo:

while resposta != 'sim':
    resposta = input('Terminou? ')


Nesse caso, não sabemos necessariamente quantas vezes
o loop será executado.

Ele pode executar:

1 vez
5 vezes
20 vezes...

Depende de quando a condição ficará False.


RESUMINDO:

for   -> "para cada elemento..."

while -> "enquanto isso for verdadeiro..."
"""


# =========================================================
# BREAK
# =========================================================

"""
=========================================================
SAINDO DE LOOPS COM BREAK
=========================================================

break significa aproximadamente:

"INTERROMPA O LOOP AGORA."


O break serve para sair de um loop antes que ele
termine normalmente.

Ele pode ser utilizado tanto com:

for

quanto com:

while
"""


# =========================================================
# BREAK - EXEMPLO 1
# =========================================================

for numero in range(1, 11):

    if numero == 6:
        break

    print(numero)

print('Saí do loop')


"""
Vamos entender:


range(1, 11)

gera:

1
2
3
4
5
6
7
8
9
10


O for começa normalmente.


numero = 1

1 == 6?

False

Então:

print(numero)


Depois:

numero = 2

2 == 6?

False


Isso continua até:

numero = 6


Agora:

6 == 6?

True


Então executamos:

break


O break fala:

"SAIA DO LOOP AGORA."


Por isso o resultado será:

1
2
3
4
5
Saí do loop


Perceba que:

6
7
8
9
10

não são impressos.

O break interrompeu o for quando numero chegou em 6.
"""


# =========================================================
# BREAK - EXEMPLO 2
# =========================================================

"""
Agora vamos usar uma estrutura muito comum:

while True


Primeiro precisamos entender:

True significa verdadeiro.


Então:

while True:

significa:

"ENQUANTO verdadeiro..."


Mas True SEMPRE é verdadeiro!

Portanto:

while True:

cria propositalmente um loop que continuaria para sempre.


Então precisamos de alguma forma de sair dele.

É aí que usamos o break.
"""


while True:

    comando = input("Digite 'sair' para sair: ")

    if comando == 'sair':
        break


"""
Funcionamento:


while True

↓


Pergunta:

Digite 'sair' para sair:


Usuário digita:

oi


Testamos:

'oi' == 'sair'?

False


Não executamos o break.

O while volta para o começo.


----------------------------------


Usuário digita:

teste


'teste' == 'sair'?

False


Continua.


----------------------------------


Usuário digita:

sair


Agora:

'sair' == 'sair'?

True


Então:

break


O break encerra o while.


Portanto:

while True

não significa necessariamente que o programa ficará
preso para sempre.

Podemos criar um critério de saída utilizando break.
"""


# =========================================================
# MELHORANDO O EXEMPLO
# =========================================================

while True:

    comando = input("Digite 'sair' para sair: ").lower()

    if comando == 'sair':
        break

    print(f'Você digitou: {comando}')

print('Programa encerrado.')


"""
Agora:

SAIR
Sair
sair
SaIr

funcionarão, pois .lower() transforma tudo em:

sair
"""


# =========================================================
# WHILE + BREAK
# =========================================================

"""
Uma estrutura MUITO comum em Python é:


while True:

    # faça alguma coisa

    if condicao:
        break


Podemos ler assim:


"Continue repetindo..."

while True:


"...até que determinada condição aconteça..."

if condicao:


"...quando acontecer, saia."

break
"""


# =========================================================
# EXEMPLO PRÁTICO - MENU
# =========================================================

while True:

    print('\n--- MENU ---')
    print('1 - Jogar')
    print('2 - Configurações')
    print('3 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print('Iniciando o jogo...')

    elif opcao == '2':
        print('Abrindo configurações...')

    elif opcao == '3':
        print('Saindo...')
        break

    else:
        print('Opção inválida.')


"""
Esse é um exemplo muito comum de uso do while.

O menu continua aparecendo enquanto o usuário quiser.

Quando ele escolhe:

3 - Sair

executamos:

break

e encerramos o loop.
"""


# =========================================================
# RESUMÃO
# =========================================================

"""
1) WHILE
---------------------------------------------------------

Significa:

"ENQUANTO"


while condicao:
    código


Exemplo:

numero = 1

while numero <= 5:
    print(numero)
    numero += 1



2) CONDIÇÃO BOOLEANA
---------------------------------------------------------

É uma expressão que resulta em:

True

ou:

False


Exemplos:

5 < 10      -> True

5 > 10      -> False

5 == 5      -> True

5 != 10     -> True



3) CRITÉRIO DE PARADA
---------------------------------------------------------

Precisamos pensar:

"O que fará meu while parar?"


Exemplo:

numero = 1

while numero <= 5:
    print(numero)
    numero += 1


O:

numero += 1

faz o número aumentar.

Eventualmente:

numero <= 5

ficará False e o loop terminará.



4) LOOP INFINITO
---------------------------------------------------------

while True:
    ...


True nunca se torna False.

Portanto precisamos normalmente de um:

break



5) BREAK
---------------------------------------------------------

Interrompe imediatamente o loop.

Exemplo:

while True:

    resposta = input("Digite sair: ")

    if resposta == "sair":
        break



6) FOR x WHILE
---------------------------------------------------------

FOR:

"Para cada elemento..."

for aluno in alunos:
    print(aluno)


WHILE:

"Enquanto essa condição for verdadeira..."

while numero < 10:
    numero += 1



FORMA DE PENSAR:

for
    ↓
"PERCORRA isso"


while
    ↓
"CONTINUE ENQUANTO isso for verdadeiro"


break
    ↓
"PARE o loop AGORA"
"""
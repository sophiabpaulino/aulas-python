"""
=========================================================
AULA - ESTRUTURAS LÓGICAS E CONDICIONAIS EM PYTHON
=========================================================

As estruturas lógicas são utilizadas para combinar, negar
ou verificar condições.

Principais operadores lógicos:

    and  -> "e"
    or   -> "ou"
    not  -> "não"

Também temos o operador:

    is   -> verifica identidade

IMPORTANTE:
'is' não funciona exatamente como um operador lógico.
Ele verifica se dois objetos são o MESMO objeto na memória.

Para comparar valores, normalmente utilizamos ==.
"""


# =========================================================
# 1. VALORES BOOLEANOS
# =========================================================

"""
Em Python existem dois valores booleanos:

    True  -> verdadeiro
    False -> falso

IMPORTANTE:
True e False começam com letra maiúscula.
"""

ativo = True
logado = False


# =========================================================
# 2. OPERADOR "and"
# =========================================================

"""
O operador 'and' significa "E".

Para uma expressão com 'and' ser True,
TODAS as condições precisam ser verdadeiras.

Tabela verdade:

True  and True  -> True
True  and False -> False
False and True  -> False
False and False -> False
"""

ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail!')


"""
No exemplo acima:

ativo = True
logado = True

Temos:

True and True -> True

Portanto, o código dentro do 'if' será executado.

Saída:

Bem-vindo usuário!
"""


# =========================================================
# 3. OPERADOR "or"
# =========================================================

"""
O operador 'or' significa "OU".

Para uma expressão com 'or' ser True,
basta que PELO MENOS UMA das condições seja verdadeira.

Ela só será False quando TODAS as condições forem False.

Tabela verdade:

True  or True  -> True
True  or False -> True
False or True  -> True
False or False -> False
"""

ativo = False
logado = False

if ativo or logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail!')


"""
Nesse caso:

ativo = False
logado = False

Temos:

False or False -> False

Por isso, o bloco do 'else' será executado.

Saída:

Você precisa ativar sua conta. Por favor, cheque seu e-mail!
"""


# =========================================================
# 4. OPERADOR "not"
# =========================================================

"""
O operador 'not' significa "NÃO".

Ele inverte o valor booleano.

not True  -> False
not False -> True

Diferentemente de 'and' e 'or', o 'not' trabalha
diretamente com uma expressão/valor, por isso é
considerado um operador unário.
"""

ativo = False
logado = False

if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail!')
else:
    print('Bem-vindo usuário!')


"""
Como:

ativo = False

Então:

not ativo
not False -> True

A condição do if é verdadeira.

Por isso será exibido:

Você precisa ativar sua conta. Por favor, cheque seu e-mail!
"""


# =========================================================
# 5. OPERADOR "is"
# =========================================================

"""
O operador 'is' verifica IDENTIDADE.

Ou seja, ele verifica se duas referências apontam
para o mesmo objeto.

Exemplo:

ativo = True

ativo is True

Nesse caso, o resultado será True.

Entretanto, é importante não confundir:

    ==  -> compara VALORES
    is  -> compara IDENTIDADE

Na maioria das comparações comuns utilizamos ==.

Exemplo:

idade = 18

idade == 18

Isso pergunta:

"O valor de idade é igual a 18?"
"""

ativo = True
logado = False

if ativo is True:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail!')
else:
    print('Bem-vindo usuário!')


"""
Como:

ativo = True

A expressão:

ativo is True

resulta em True.

Então o primeiro print será executado.

OBSERVAÇÃO:

Apesar de funcionar, normalmente não precisamos escrever:

if ativo is True:

Podemos simplesmente escrever:

if ativo:

Da mesma forma, em vez de:

if ativo is False:

podemos utilizar:

if not ativo:
"""



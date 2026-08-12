"""
TIPOS NUMÉRICOS E OPERAÇÕES EM PYTHON
======================================

Python possui tipos numéricos, sendo os principais:

int   -> números inteiros
float -> números com casas decimais

Exemplos:

numero_inteiro = 42
numero_decimal = 2.5


1. OPERAÇÕES ARITMÉTICAS
------------------------

ADIÇÃO (+)

Soma dois valores.

Exemplo:
5 + 4
Resultado: 9


SUBTRAÇÃO (-)

Subtrai um valor de outro.

Exemplo:
7 - 2
Resultado: 5


MULTIPLICAÇÃO (*)

Multiplica dois valores.

Exemplo:
3 * 5
Resultado: 15


DIVISÃO (/)

Realiza uma divisão normal.

IMPORTANTE:
O operador / retorna um número do tipo float,
mesmo quando a divisão é exata.

Exemplo:
5 / 2
Resultado: 2.5

Outro exemplo:
10 / 2
Resultado: 5.0


DIVISÃO INTEIRA (//)

Realiza a divisão e retorna apenas a parte inteira
do resultado (arredondando para baixo).

Exemplo:
5 // 2
Resultado: 2


MÓDULO (%)

Retorna o RESTO de uma divisão.

É muito utilizado para descobrir, por exemplo,
se um número é par ou ímpar.

Exemplos:

4 % 2
Resultado: 0

5 % 2
Resultado: 1

7 % 2
Resultado: 1

8 % 2
Resultado: 0

Se:
numero % 2 == 0
o número é par.

Se:
numero % 2 == 1
o número é ímpar.


EXPONENCIAÇÃO (**)

Eleva um número a uma potência.

Exemplo:

3 ** 3
Resultado: 27

Significa:
3 * 3 * 3 = 27


Outro exemplo:

2 ** 8
Resultado: 256


Python consegue trabalhar com números inteiros
muito grandes.


Exemplo:

2 ** 63
Resultado: 9223372036854775808


2. CONVERSÃO DE NÚMEROS
-----------------------

Podemos converter um valor para inteiro utilizando int().

Exemplo:

5 / 2
Resultado: 2.5

int(5 / 2) -> O CAST
Resultado: 2

O int() converte o resultado para um número inteiro.

ATENÇÃO:
int() não arredonda normalmente.
Ele remove a parte decimal.

Exemplo:

int(2.9)
Resultado: 2


3. SEPARADOR DE MILHAR COM UNDERSCORE
-------------------------------------

Python permite utilizar _ (underline) para facilitar
a leitura de números grandes.

Exemplo:

1000000

Pode ser escrito como:

1_000_000

Os dois representam exatamente o mesmo número.

Exemplo:

1_000_000
Resultado: 1000000

Também podemos fazer:

1_000_000_000
Resultado: 1000000000

O underline serve apenas para melhorar a leitura
do código. Ele não altera o valor do número.


4. VARIÁVEIS NUMÉRICAS
----------------------

Podemos guardar números dentro de variáveis.

Exemplo:

num = 42

Ao acessar:

num

Resultado:
42


Também podemos realizar operações utilizando
a variável.

Exemplo:

num + 1

Resultado:
43


IMPORTANTE:

Fazer:

num + 1

NÃO altera o valor armazenado em num.

Apenas calcula o resultado.

Para alterar a variável precisamos fazer:

num = num + 1

ou utilizar os operadores de atribuição.


5. OPERADORES DE ATRIBUIÇÃO
---------------------------

+=  -> soma e atribui
-=  -> subtrai e atribui
*=  -> multiplica e atribui
/=  -> divide e atribui
//= -> divisão inteira e atribui
%=  -> calcula o resto e atribui
**= -> calcula a potência e atribui


Exemplo:

num = 42

num += 1

É a forma reduzida de escrever:

num = num + 1

Agora:
num = 43


SUBTRAÇÃO:

num -= 1

É equivalente a:

num = num - 1


MULTIPLICAÇÃO:

num *= 2

É equivalente a:

num = num * 2


DIVISÃO:

num /= 2

É equivalente a:

num = num / 2

IMPORTANTE:
A divisão com / normalmente transforma o
resultado em float.

Exemplo:

num = 86

num /= 2

Resultado:
43.0


DIVISÃO INTEIRA:

num //= 2

É equivalente a:

num = num // 2


6. RESUMO DOS OPERADORES
------------------------

+   -> Adição

-   -> Subtração

*   -> Multiplicação

/   -> Divisão

//  -> Divisão inteira

%   -> Módulo (resto da divisão)

**  -> Potência


Operadores com atribuição:

+=
-=
*=
/=
//=
%=
**=


Exemplos rápidos:

5 + 4   -> 9

7 - 2   -> 5

3 * 5   -> 15

5 / 2   -> 2.5

5 // 2  -> 2

5 % 2   -> 1

3 ** 3  -> 27
"""
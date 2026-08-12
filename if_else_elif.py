"""
Estruturas condicionais

if (se), else, elif (else if)

As estruturas condicionais permitem que o programa tome decisões
dependendo se determinada condição é verdadeira ou falsa.

if   -> se
elif -> senão, se...
else -> senão
"""


idade = 18


"""
Estrutura condicional if, else em C:

if(idade < 18){
    printf("Menor de idade");
}else if(idade == 18){
    printf("Tem 18 anos");
}else{
    printf("É maior de idade");
}
"""


"""
Estrutura condicional if, else em Java:

if(idade < 18){
    System.out.println("Menor de idade");
}else if(idade == 18){
    System.out.println("Tem 18 anos");
}else{
    System.out.println("É maior de idade");
}
"""


# Estrutura condicional em Python:

if idade < 18:
    print('Menor de idade')

elif idade == 18:
    print('Tem 18 anos')

elif idade == 26:
    print('Tem 26 anos')

else:
    print('Maior de idade')


"""
OBSERVAÇÕES IMPORTANTES:

1. O if inicia uma estrutura condicional.

2. O elif significa "else if", ou seja:
   "senão, se essa outra condição for verdadeira..."

3. O else é executado caso nenhuma das condições anteriores
   seja verdadeira.

4. O else não recebe uma condição.

5. Quando uma condição de uma estrutura if/elif/else é verdadeira,
   o Python executa aquele bloco e não verifica os próximos elif/else.

6. Em Python, a indentação é obrigatória.
   Normalmente utilizamos 4 espaços.


OPERADORES DE COMPARAÇÃO:

==  -> igual a
!=  -> diferente de
>   -> maior que
<   -> menor que
>=  -> maior ou igual a
<=  -> menor ou igual a


ATENÇÃO:

= significa ATRIBUIÇÃO

Exemplo:

idade = 18

Estamos colocando o valor 18 na variável idade.


== significa COMPARAÇÃO

Exemplo:

idade == 18

Estamos perguntando:
"idade é igual a 18?"

Essa comparação terá como resultado True ou False.
"""
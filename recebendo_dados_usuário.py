'''
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> \'''Angelina Jolie\'''
- Aspas duplas triplas -> """Angelina Jolie"""


# ENTRADA DE DADOS <<<<<<<<<<<<<<<<<<<<<<<<<<

print("Qual seu nome? ")
nome = input()  # Input -> Entrada

nome = input('Qual seu nome? ')

idade = input('Qual sua idade? ')

# PROCESSAMENTO <<<<<<<<<<<<

(usuário inserir os dados)

# SAÍDA <<<<<<<<<<<<<<<<<<<<<<


# Exemplo de print 'antigo' 2.x

print('A %s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x

print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'A {nome} tem {idade} anos') <<<<<<<<<<<< MAIS UTILIZADO 


# int(idade) => cast
Cast é a 'conversão' de um tipo de dado para outro.


print(f'A {nome} nasceu em {2018 - int(idade)}')

'''
"""

LABORATÓRIO 01 - AULA 02


# ---------------------------------------------------------------------
# TUPLA — usada para representar uma PERCEPÇÃO.
# ---------------------------------------------------------------------

# Criamos a tupla: dois valores entre parênteses, separados por vírgula.
percepcao = ("A", "Sujo")

print("A percepção completa:", percepcao)
print("Quantos elementos ela tem?", len(percepcao))   # len() conta os elementos

# Acesso por POSIÇÃO. Atenção: em Python a contagem começa em ZERO,
# então o primeiro elemento é [0] e o segundo é [1].
print("Elemento na posição 0:", percepcao[0])
print("Elemento na posição 1:", percepcao[1])

# DESEMPACOTAMENTO: quebra a tupla em duas variáveis de uma só vez.
# À esquerda do "=" colocamos tantos nomes quantos forem os elementos.
local_atual, estado_atual = percepcao

print("Depois do desempacotamento -> local:", local_atual, "| estado:", estado_atual)

# A tupla é IMUTÁVEL: a linha abaixo daria erro se fosse executada.
# Descomente para ver o TypeError acontecer — errar de propósito ensina.
# percepcao[0] = "B"

# ---------------------------------------------------------------------
# LISTA — usada para o conjunto de AÇÕES e para históricos.
# ---------------------------------------------------------------------

# Criamos a lista com três ações. Colchetes, e não parênteses.
acoes = ["Aspirar", "Direita", "Esquerda"]
print("Ações iniciais:", acoes)

# append() ACRESCENTA um elemento ao final. Repare que a lista MUDA:
# é a diferença fundamental em relação à tupla.
acoes.append("NadaFazer")
print("Depois do append:", acoes)

# Acesso por posição, igual à tupla: começa em zero.
print("Primeira ação :", acoes[0])

# Índice NEGATIVO conta de trás para frente: -1 é o último elemento.
# Isso evita escrever acoes[len(acoes) - 1], que é mais longo e mais frágil.
print("Última ação   :", acoes[-1])

print("Total de ações:", len(acoes))

# O operador "in" verifica se um valor está na lista. Devolve True ou False.
# É assim que o agente pergunta: "esta ação é permitida?"
print("'Aspirar' é uma ação válida?", "Aspirar" in acoes)
print("'Voar' é uma ação válida?   ", "Voar" in acoes)

# ---------------------------------------------------------------------
# DICIONÁRIO — usado para representar o ESTADO DO MUNDO.
#
# Estrutura: {chave: valor, chave: valor}
# Aqui, cada chave é um local do ambiente e cada valor é a condição
# daquele local. Este dicionário é, literalmente, o estado do mundo
# do aspirador num dado instante.
# ---------------------------------------------------------------------

mundo = {"A": "Sujo", "B": "Limpo"}
print("Estado do mundo:", mundo)

# LEITURA por chave: usamos o NOME entre colchetes, não um número.
print("O local A está:", mundo["A"])
print("O local B está:", mundo["B"])

# ESCRITA: atribuir a uma chave existente ALTERA o valor.
# É assim que a ação "Aspirar" modifica o ambiente.
mundo["A"] = "Limpo"
print("Depois de aspirar A:", mundo)

# .keys() devolve as chaves; .values() devolve os valores.
print("Locais existentes  :", list(mundo.keys()))
print("Condições dos locais:", list(mundo.values()))

# .get() consulta com segurança: devolve None se a chave não existir,
# em vez de interromper o programa com KeyError.
print("E o local C?", mundo.get("C"))

# ---------------------------------------------------------------------
# FUNÇÃO — a estrutura que representa o PROGRAMA DO AGENTE.
#
# Esta primeira função é simples de propósito: ela apenas informa
# quanto custa executar cada ação. Usaremos isso mais adiante, quando
# a medida de desempenho passar a penalizar movimento.
# ---------------------------------------------------------------------

def custo_da_acao(acao):
    Devolve o custo de executar uma ação: 0 para NadaFazer, 1 para as demais.

    Parâmetro:
        acao (str): o nome da ação, por exemplo "Aspirar".

    Devolve:
        int: o custo da ação.

    # A comparação usa DOIS sinais de igual (==). Um sinal só (=) é
    # atribuição; dois são comparação. Trocar os dois é erro clássico.
    if acao == 'NadaFazer':
        return 0        # return encerra a função AQUI; nada abaixo executa

    # Se a execução chegou nesta linha, é porque o if acima foi falso.
    return 1


# Chamando a função: escrevemos o nome e passamos o argumento entre parênteses.
print("Custo de 'Aspirar'  :", custo_da_acao("Aspirar"))
print("Custo de 'NadaFazer':", custo_da_acao("NadaFazer"))

# ---------------------------------------------------------------------
# LAÇOS — percorrendo listas e dicionários.
# ---------------------------------------------------------------------

# Laço sobre uma LISTA: a variável "acao" assume um valor por vez.
print("Custo de cada ação:")
for acao in acoes:
    # f-string: o texto começa com f e as variáveis vão entre chaves.
    # :12s alinha o texto em 12 caracteres, deixando a saída em colunas.
    print(f"  {acao:12s} -> custo {custo_da_acao(acao)}")

print()   # print() sem argumentos apenas pula uma linha

# Laço sobre um DICIONÁRIO com .items(): recebemos chave e valor de uma vez.
print("Situação de cada local:")
for lugar, estado in mundo.items():
    print(f"  O local {lugar} está {estado}.")

-------------------------------------------------------------------------------
    Contar quantos locais do mundo estão sujos.
    Parâmetro:
        mundo (dict): dicionário local -> condição, ex. {"A": "Sujo"}.

    Devolve:
        int: a quantidade de locais sujos.
-------------------------------------------------------------------------------
    def conta_sujos(mundo): -> MUNDO (parâmetro da função)
    
# DUAS FROMAS EQUIVALENTES DE FAZER O DICIONÁRIO DO PARÂMETRO MUNDO

1)   meu_mundo = {"A": "Sujo", "B": "Sujo"}

     conta_sujos(meu_mundo)
    
2)   conta_sujos({"A": "Sujo", "B": "Sujo"})
    
    
    
    quantidades_sujos = 0 -> contador de locais sujos

    for valor in mundo.values():
        if valor == "Sujo":
            quantidades_sujos += 1

    return quantidades_sujos
"""

# EXERCÍCIO 01

# 1. Definição do Mundo Inicial
mundo = {"Setor_A": "Com_Pacote", "Setor_B": "Vazio"}


# 2. Função do Agente
def agente_com_memoria(percepcao, memoria):
    local, estado = percepcao
    memoria[local] = estado

    if estado == "Com_Pacote":
        memoria[local] = "Vazio"
        return "Coletar"

    outro_setor = "Setor_B" if local == "Setor_A" else "Setor_A"

    if memoria.get(outro_setor) == "Vazio":
        return "Aguardar"
    else:
        return "Mover"


# 3. Função do Simulador
def simular_passo(agente, mundo, local_atual, memoria):
    percepcao = (local_atual, mundo[local_atual])
    acao = agente(percepcao, memoria)

    if acao == "Coletar":
        mundo[local_atual] = "Vazio"
    elif acao == "Mover":
        local_atual = "Setor_B" if local_atual == "Setor_A" else "Setor_A"

    return local_atual, acao


# 4. EXECUTANDO E IMPRIMINDO O TESTE
memoria_agente = {}
local_robo = "Setor_A"

print("--- INÍCIO DA SIMULAÇÃO ---", flush=True)
print("Mundo Inicial:", mundo, flush=True)

# Passo 1
local_robo, acao1 = simular_passo(
    agente_com_memoria, mundo, local_robo, memoria_agente
)
print(f"Passo 1 -> Ação: {acao1:8s} | Posição Robô: {local_robo}", flush=True)

# Passo 2
local_robo, acao2 = simular_passo(
    agente_com_memoria, mundo, local_robo, memoria_agente
)
print(f"Passo 2 -> Ação: {acao2:8s} | Posição Robô: {local_robo}", flush=True)

# Passo 3
local_robo, acao3 = simular_passo(
    agente_com_memoria, mundo, local_robo, memoria_agente
)
print(f"Passo 3 -> Ação: {acao3:8s} | Posição Robô: {local_robo}", flush=True)

print("\nMundo Final:", mundo, flush=True)
print("Memória do Agente:", memoria_agente, flush=True)
print("--- FIM DA SIMULAÇÃO ---", flush=True)
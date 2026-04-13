# Solicita o nome do aluno
nome = input("Digite o nome do aluno: ")

# Solicita as três notas
nota_prova = float(input("Digite a nota da prova: "))
nota_trabalho = float(input("Digite a nota do trabalho: "))
nota_projeto = float(input("Digite a nota do projeto: "))

# Define os pesos
peso_prova = 5
peso_trabalho = 3
peso_projeto = 2

# Calcula a média ponderada
# A fórmula é: ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3)
soma_pesos = peso_prova + peso_trabalho + peso_projeto
media = ((nota_prova * peso_prova) + (nota_trabalho * peso_trabalho) + (nota_projeto * peso_projeto)) / soma_pesos

# Exibe o resultado usando f-string, formatando a média para uma casa decimal
print(f"O aluno {nome} obteve média {media:.1f}")
 

# Entrada de dados: Lendo largura e altura como números reais
largura = float(input("Digite a largura da parede (em metros): "))
altura = float(input("Digite a altura da parede (em metros): "))

# Definição do valor fixo por metro quadrado
preco_por_metro = 25.00

# Processamento: Cálculo da área e do custo total
area = largura * altura
custo_total = area * preco_por_metro

# Saída: Exibindo os resultados com f-string
# O código :.2f formata os valores para duas casas decimais
print(f"A parede possui uma área de {area:.2f}m² e o custo total da pintura será de R$ {custo_total:.2f}")
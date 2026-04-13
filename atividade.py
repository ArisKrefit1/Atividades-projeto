### --- BLOCO 1: VARIÁVEIS E TIPOS --- ###
nome_produto = "Monitor Gamer"
preco = 1200.50
disponivel = True

print(f"Produto: {nome_produto} | Tipo: {type(nome_produto)}")
print(f"Preço: {preco} | Tipo: {type(preco)}")
print(f"Disponível: {disponivel} | Tipo: {type(disponivel)}")

### --- BLOCO 2: CÁLCULOS GEOMÉTRICOS E STRINGS --- ###
base = 5
altura = 3
area = base * altura
print(f"\nA área do retângulo é: {area}")

usuario = "Ana"
mensagem = "Bem-vindo, " + usuario
print(mensagem)

### --- BLOCO 3: OPERADORES ARITMÉTICOS E POTÊNCIA --- ###
resto = 17 % 5
print(f"\nO resto de 17 dividido por 5 é: {resto}")

# Demonstração de tipagem dinâmica
num = 10
print(f"Tipo inicial: {type(num)}")
num = "10"
print(f"Tipo após mudar para string: {type(num)}")
num = True
print(f"Tipo após mudar para bool: {type(num)}")

# Potência
res_op = 2 ** 8
res_pow = pow(2, 8)
print(f"2 elevado a 8: {res_op} (Operador) | {res_pow} (Função pow)")

### --- BLOCO 4: ATRIBUIÇÃO COMPOSTA E CONSTANTES --- ###
contador = 10
contador += 5
contador *= 2
contador -= 8
contador /= 3
print(f"\nValor final do contador: {contador:.2f}")

TAXA_CONVERSAO = 5.20
print(f"US$ 100 -> R$ {100 * TAXA_CONVERSAO:.2f}")
print(f"US$ 250 -> R$ {250 * TAXA_CONVERSAO:.2f}")
print(f"US$ 500 -> R$ {500 * TAXA_CONVERSAO:.2f}")

### --- BLOCO 5: DECOMPOSIÇÃO E ESTÉTICA --- ###
total_segundos = 3725
horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60
print(f"\nTempo decomposto: {horas}h {minutos}m {segundos}s")

print("=" * 30)
print("RELATÓRIO DE VENDAS".center(30))
print("=" * 30)

### --- BLOCO 6: ENTRADAS DO USUÁRIO (INTERATIVO) --- ###
# Média UFERSA
n1 = float(input("\nDigite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
media = (n1 + n2 + n3) / 3
print(f"Média Parcial: {media:.2f}")

# Saque Eletrônico
valor_saque = int(input("\nValor para saque: "))
n50 = valor_saque // 50
resto_saque = valor_saque % 50
n20 = resto_saque // 20
n10 = (resto_saque % 20) // 10
print(f"Notas entregues: {n50} de R$50, {n20} de R$20, {n10} de R$10")

# Expressão Matemática Complexa
vx = float(input("\nDigite x para a expressão: "))
vy = float(input("Digite y para a expressão: "))
z = (pow(vx, 2) + pow(vy, 2)) * pow(vx * vy, -1)
print(f"Resultado de z: {z} | Tipo: {type(z)}")
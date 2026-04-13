def menu():
    while True:
        print("\n" + "="*40)
        print("      SISTEMA MULTIFUNCIONAL")
        print("="*40)
        print("1. Média Ponderada")
        print("2. Cálculo de Pintura")
        print("3. Fluxo de Caixa")
        print("4. Projeção Financeira")
        print("5. Resumo de Estoque")
        print("6. Atualização de Inventário")
        print("7. Cálculo de Desconto")
        print("8. Comissão de Vendedor")
        print("9. Aluguel Proporcional")
        print("10. Simulação de Financiamento")
        print("0. Sair")
        print("="*40)
        
        opcao = input("Escolha uma opção (ou '0' para sair): ")

        if opcao == '0':
            print("Saindo do sistema...")
            break

        # A partir daqui, cada opção tem um pequeno check para voltar
        print("\n(Dica: Para cancelar e voltar ao menu, deixe o campo vazio e aperte Enter)")
        
        try:
            if opcao == '1':
                nome = input("Nome do aluno: ")
                if not nome: continue # Volta ao menu se estiver vazio
                
                n1 = float(input("Nota da prova: "))
                n2 = float(input("Nota do trabalho: "))
                n3 = float(input("Nota do projeto: "))
                media = ((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10
                print(f"\nO aluno {nome} obteve média {media:.1f}")

            elif opcao == '2':
                l = float(input("Largura (m): "))
                a = float(input("Altura (m): "))
                area = l * a
                print(f"\nÁrea: {area:.2f}m² | Custo: R$ {area * 25:.2f}")

            elif opcao == '3':
                v_vista = float(input("Vendas à vista: "))
                v_prazo = float(input("Vendas a prazo: "))
                desp = float(input("Despesas: "))
                receita = v_vista + v_prazo
                print(f"\nReceita: R$ {receita:.2f} | Saldo: R$ {receita - desp:.2f}")

            elif opcao == '4':
                medio = float(input("Saldo médio: R$ "))
                dias = int(input("Dias úteis: "))
                print(f"\nProjeção: R$ {medio * dias:.2f}")

            elif opcao == '5':
                total_geral = 0
                for i in range(1, 4):
                    qtd = int(input(f"Qtd Produto {i}: "))
                    val = float(input(f"Valor Unit. Produto {i}: "))
                    total_geral += (qtd * val)
                print(f"\nTotal Estoque: R$ {total_geral:.2f}")

            elif opcao == '6':
                estoque = int(input("Estoque Inicial: "))
                estoque += int(input("Qtd Comprada: "))
                estoque -= int(input("Qtd Vendida: "))
                print(f"\nEstoque Atualizado: {estoque}")

            elif opcao == '7':
                qtd = int(input("Quantidade: "))
                preco = float(input("Preço Unitário: "))
                bruto = qtd * preco
                print(f"\nFinal com 10% desc: R$ {bruto * 0.90:.2f}")

            elif opcao == '8':
                fixo = float(input("Salário Fixo: "))
                vendas = float(input("Total Vendas: "))
                print(f"\nTotal com Comissão: R$ {fixo + (vendas * 0.05):.2f}")

            elif opcao == '9':
                dias = int(input("Dias ocupados: "))
                print(f"\nPro Rata (30 dias): R$ {(2400/30)*dias:.2f}")

            elif opcao == '10':
                imovel = float(input("Valor Imóvel: "))
                entrada = float(input("Entrada: "))
                parc = int(input("Parcelas: "))
                taxa = float(input("Taxa Juros (%): "))
                finan = imovel - entrada
                parcela = (finan / parc) + (finan * (taxa/100))
                print(f"\nParcela Estimada: R$ {parcela:.2f}")

            else:
                print("Opção inválida!")

        except ValueError:
            # Se o usuário apertar Enter vazio ou digitar letras onde devia ser número
            print("\n>> Operação cancelada ou dado inválido. Retornando ao menu...")
            continue

if __name__ == "__main__":
    menu()
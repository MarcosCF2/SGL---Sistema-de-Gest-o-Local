from Storage import carregar_dados, salvar_dados
from utils import ler_opcao_menu
from Produtos import cadastrar_produto, listar_produtos, buscar_produto_menu, editar_produto
from movimentacoes import registrar_mov, relatorio_movimentacoes
from Relatorio import relatorio_gerencial, exportar_relatorio_txt, filtrar_por_categoria



def exibir_menu():
    print("\n" + "=" * 50)
    print("   SGL - Sistema de Gestao Local")
    print("=" * 50)
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Buscar produto por nome")
    print("4. Registrar ENTRADA de estoque")
    print("5. Registrar SAIDA de estoque")
    print("6. Relatorio de movimentacoes")
    print("7. Relatorio gerencial (estatisticas)")
    print("8. Salvar e sair")
    print("=" * 50)
    print("[B] Bonus - Editar produto")
    print("[C] Bonus - Filtrar por categoria")
    print("[E] Bonus - Exportar relatorios TXT")
    print("=" * 50)


def executar_opcao_bonus(entrada, produtos, movs):
    """Trata as opcoes bonus do menu."""
    op = entrada.upper()

    if op == "B":
        editar_produto(produtos)
        return True
    if op == "C":
        filtrar_por_categoria(produtos, movs)
        return True
    if op == "E":
        exportar_relatorio_txt(produtos, movs)
        return True

    return False


def main():
    print("\nIniciando SGL - Sistema de Gestao Local")
    produtos, movs = carregar_dados()
    print(
        f"{len(produtos)} produto(s) e "
        f"{len(movs)} movimentacao(oes) carregada(s)."
    )

    while True:
        exibir_menu()
        entrada = input("\nEscolha uma opcao (1-8 ou B/C/E): ").strip()

        if executar_opcao_bonus(entrada, produtos, movs):
            continue

        try:
            opcao = int(entrada)
        except ValueError:
            print("[!] Opcao invalida.")
            continue

        if opcao < 1 or opcao > 8:
            print("[!] Opcao invalida. Escolha entre 1 e 8.")
            continue

        if opcao == 1:
            cadastrar_produto(produtos)
        elif opcao == 2:
            listar_produtos(produtos)
        elif opcao == 3:
            buscar_produto_menu(produtos)
        elif opcao == 4:
            registrar_mov(produtos, movs, "E")
        elif opcao == 5:
            registrar_mov(produtos, movs, "S")
        elif opcao == 6:
            relatorio_movimentacoes(produtos, movs)
        elif opcao == 7:
            relatorio_gerencial(produtos, movs)
        elif opcao == 8:
            print("\nSalvando dados...")
            salvar_dados(produtos, movs)
            print("Ate logo!")
            break


if __name__ == "__main__":
    main()

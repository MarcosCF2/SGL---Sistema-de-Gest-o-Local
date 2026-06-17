from utils import ler_int, ler_str
from Produtos import proximo_id, buscar_produto_por_id, listar_produtos  


def registrar_mov(produto, movs, tipo):
    """F7 — Registra entrada ('E') ou saída ('S') de estoque."""
    tipo = tipo.upper()
    titulo = "ENTRADA DE ESTOQUE" if tipo == "E" else "SAÍDA DE ESTOQUE"

    print("\n" + "=" * 50)
    print(f"  {titulo}")
    print("=" * 50)

    if not produto:
        print("  Nenhum produto cadastrado. Cadastre produtos primeiro.")
        return



    proximo_id = ler_int("\n  ID do produto: ", minimo=1)
    produto = buscar_produto_por_id(produto, proximo_id)

    if not produto:
        print(f"  [!] Produto com ID {proximo_id} não encontrado.")
        return

    print(f"  Produto: {produto['nome']} | Estoque atual: {produto['estoque']}")

    # Quantidade com validação de estoque para saída
    while True:
        quantidade = ler_int("  Quantidade: ", minimo=1)
        if tipo == "S" and quantidade > produto["estoque"]:
            print(
                f"  [!] Estoque insuficiente! Disponível: {produto['estoque']}. "
                f"Tente novamente."
            )
            continue
        break

    data = ler_str("  Data (ex.: 2026-06-14): ")
    observacao = ler_str("  Observação (opcional, Enter para pular): ", obrigatorio=False)

    mov = {
        "id": proximo_id(movs),
        "produto_id": proximo_id,
        "tipo": tipo,
        "quantidade": quantidade,
        "data": data,
        "observacao": observacao,
    }
    movs.append(mov)

    # Atualiza estoque
    if tipo == "E":
        produto["estoque"] += quantidade
        print(f"\n  [✓] Entrada registrada. Novo estoque: {produto['estoque']}")
    else:
        produto["estoque"] -= quantidade
        print(f"\n  [✓] Saída registrada. Novo estoque: {produto['estoque']}")


def relatorio_movimentacoes(produto, movs):
    """Opção 6 — Lista movimentações com totalizações."""
    print("\n" + "=" * 80)
    print("  RELATÓRIO DE MOVIMENTAÇÕES")
    print("=" * 80)

    if not movs:
        print("  Nenhuma movimentação registrada.")
        return

    total_entradas = 0
    total_saidas = 0

    print(
        f"  {'ID':<5} {'Data':<12} {'Tipo':<6} {'Prod.ID':<8} "
        f"{'Produto':<20} {'Qtd':>6}  {'Obs.'}"
    )
    print("  " + "-" * 75)

    for m in movs:
        produto = buscar_produto_por_id(produto, m["proximo_id"])
        nome_produto = produto["nome"] if produto else "(removido)"
        tipo_label = "ENTRADA" if m["tipo"] == "E" else "SAÍDA  "
        obs = m.get("observacao", "") or "-"

        print(
            f"  {m['id']:<5} {m['data']:<12} {tipo_label:<6} {m['proximo_id']:<8} "
            f"{nome_produto:<20} {m['quantidade']:>6}  {obs}"
        )

        if m["tipo"] == "E":
            total_entradas += m["quantidade"]
        else:
            total_saidas += m["quantidade"]

    print("=" * 80)
    print(f"  Total de ENTRADAS (unidades): {total_entradas}")
    print(f"  Total de SAÍDAS  (unidades): {total_saidas}")
    print(f"  Saldo líquido              : {total_entradas - total_saidas}")

from Produtos import buscar_produto_por_id


def relatorio_gerencial(produtos, movs):
    """F8 — Gera estatísticas completas do estoque."""
    print("\n" + "=" * 60)
    print("  RELATÓRIO GERENCIAL")
    print("=" * 60)

    if not produtos:
        print("  Nenhum produto cadastrado.")
        return

    # --- Maior e menor estoque ---
    maior_estoque = max(p["estoque"] for p in produtos)
    menor_estoque = min(p["estoque"] for p in produtos)

    maiores = [p for p in produtos if p["estoque"] == maior_estoque]
    menores = [p for p in produtos if p["estoque"] == menor_estoque]

    print("\n  [ ESTOQUE MÁXIMO ]")
    for p in maiores:
        print(f"    → {p['nome']} (ID {p['id']}) — {p['estoque']} unidades")

    print("\n  [ ESTOQUE MÍNIMO ]")
    for p in menores:
        print(f"    → {p['nome']} (ID {p['id']}) — {p['estoque']} unidades")

    # --- Valor total do estoque ---
    valor_total = sum(p["estoque"] * p["preco"] for p in produtos)
    print(f"\n  [ VALOR TOTAL DO ESTOQUE ]")
    print(f"    R$ {valor_total:,.2f}")

    # --- Quantidade de produtos por categoria ---
    categorias = {}
    for p in produtos:
        cat = p["categoria"]
        categorias[cat] = categorias.get(cat, 0) + 1

    print("\n  [ PRODUTOS POR CATEGORIA ]")
    for cat, qtd in sorted(categorias.items()):
        print(f"    {cat:<15}: {qtd} produto(s)")

    # --- Top 3 produtos com maior valor em estoque ---
    top3 = sorted(produtos, key=lambda p: p["estoque"] * p["preco"], reverse=True)[:3]
    print("\n  [ TOP 3 — MAIOR VALOR EM ESTOQUE ]")
    for i, p in enumerate(top3, 1):
        valor = p["estoque"] * p["preco"]
        print(f"    {i}. {p['nome']:<25} — R$ {valor:,.2f} ({p['estoque']} un × R$ {p['preco']:.2f})")

    print("=" * 60)


def exportar_relatorio_txt(produtos, movs):
    """Bônus — Exporta relatório completo em arquivo TXT."""
    linhas = []
    linhas.append("=" * 60)
    linhas.append("  SGL — RELATÓRIO EXPORTADO")
    linhas.append("=" * 60)

    # Produtos
    linhas.append("\n  LISTA DE PRODUTOS\n")
    linhas.append(f"  {'ID':<5} {'Nome':<25} {'Categoria':<12} {'Preço':>10} {'Estoque':>8}")
    linhas.append("  " + "-" * 65)
    for p in sorted(produtos, key=lambda x: x["nome"].lower()):
        linhas.append(
            f"  {p['id']:<5} {p['nome']:<25} {p['categoria']:<12} "
            f"R$ {p['preco']:>8.2f} {p['estoque']:>8}"
        )

    # Movimentações
    linhas.append("\n\n  MOVIMENTAÇÕES\n")
    linhas.append(
        f"  {'ID':<5} {'Data':<12} {'Tipo':<8} {'Prod.ID':<8} {'Produto':<20} {'Qtd':>6}"
    )
    linhas.append("  " + "-" * 65)
    total_e = 0
    total_s = 0
    for m in movs:
        produto = buscar_produto_por_id(produtos, m["produto_id"])
        nome = produto["nome"] if produto else "(removido)"
        tipo_label = "ENTRADA" if m["tipo"] == "E" else "SAÍDA"
        linhas.append(
            f"  {m['id']:<5} {m['data']:<12} {tipo_label:<8} {m['produto_id']:<8} "
            f"{nome:<20} {m['quantidade']:>6}"
        )
        if m["tipo"] == "E":
            total_e += m["quantidade"]
        else:
            total_s += m["quantidade"]
    linhas.append(f"\n  Total entradas: {total_e} | Total saídas: {total_s}")

    # Estatísticas
    if produtos:
        valor_total = sum(p["estoque"] * p["preco"] for p in produtos)
        linhas.append(f"\n  Valor total do estoque: R$ {valor_total:,.2f}")

    nome_arquivo = "relatorio.txt"
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write("\n".join(linhas))
        print(f"  [✓] Relatório exportado para '{nome_arquivo}'.")
    except IOError as e:
        print(f"  [!] Erro ao exportar relatório: {e}")


def filtrar_por_categoria(produtos):
    """Bônus — Lista produtos filtrados por categoria."""
    print("\n" + "=" * 50)
    print("  FILTRO POR CATEGORIA")
    print("=" * 50)

    if not produtos:
        print("  Nenhum produto cadastrado.")
        return

    categorias = sorted(set(p["categoria"] for p in produtos))
    print("  Categorias disponíveis:")
    for i, cat in enumerate(categorias, 1):
        print(f"    {i}. {cat}")

    idx = None
    while True:
        try:
            idx = int(input("  Escolha (número): ").strip())
            if 1 <= idx <= len(categorias):
                break
            print(f"  [!] Escolha entre 1 e {len(categorias)}.")
        except ValueError:
            print("  [!] Entrada inválida.")

    categoria_escolhida = categorias[idx - 1]
    filtrados = [p for p in produtos if p["categoria"] == categoria_escolhida]

    print(f"\n  Produtos na categoria '{categoria_escolhida}':\n")
    print(f"  {'ID':<5} {'Nome':<25} {'Preço':>10} {'Estoque':>8}")
    print("  " + "-" * 52)
    for p in filtrados:
        print(f"  {p['id']:<5} {p['nome']:<25} R$ {p['preco']:>8.2f} {p['estoque']:>8}")

from utils import ler_int, ler_float, ler_str

CATEGORIAS = ["Alimento", "Limpeza", "Higiene", "Eletrônico", "Outros"]


def proximo_id(lista):
    """F5 — Retorna o próximo ID disponível (maior id + 1, ou 1 se vazio)."""
    if not lista:
        return 1
    return max(item["id"] for item in lista) + 1


def buscar_produtos(produtos, texto):
    """F6 — Retorna lista de produtos cujo nome contém o texto (case-insensitive)."""
    texto = texto.strip().lower()
    return [p for p in produtos if texto in p["nome"].lower()]


def buscar_produto_por_id(produtos, produto_id):
    """Retorna o produto com o id informado, ou None se não encontrado."""
    for p in produtos:
        if p["id"] == produto_id:
            return p
    return None


def _escolher_categoria():
    """Exibe categorias e solicita escolha."""
    print("\n  Categorias disponíveis:")
    for i, cat in enumerate(CATEGORIAS, 1):
        print(f"    {i}. {cat}")
    idx = ler_int("  Escolha a categoria (número): ", 1, len(CATEGORIAS))
    return CATEGORIAS[idx - 1]


def cadastrar_produto(produto):
    """Opção 1 — Cadastra um novo produto."""
    print("\n" + "=" * 50)
    print("  CADASTRAR PRODUTO")
    print("=" * 50)

    nome = ler_str("  Nome do produto: ")

    # Verifica duplicidade de nome
    existentes = buscar_produtos(produto, nome)
    exatos = [p for p in existentes if p["nome"].lower() == nome.lower()]
    if exatos:
        print(f"  [!] Já existe um produto com o nome '{nome}' (ID {exatos[0]['id']}).")
        confirmar = ler_str("  Deseja cadastrar mesmo assim? (s/n): ").lower()
        if confirmar != "s":
            print("  Cadastro cancelado.")
            return

    categoria = _escolher_categoria()
    preco = ler_float("  Preço unitário (R$): ", minimo=0.0)
    estoque = ler_int("  Estoque inicial: ", minimo=0)

    novo = {
        "id": proximo_id(produto),
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "estoque": estoque,
    }
    produto.append(novo)
    print(f"\n  [✓] Produto '{nome}' cadastrado com ID {novo['id']}.")


def listar_produtos(produto):
    """Opção 2 — Lista todos os produtos ordenados por nome (bônus)."""
    print("\n" + "=" * 70)
    print("  LISTA DE PRODUTOS")
    print("=" * 70)

    if not produto:
        print("  Nenhum produto cadastrado.")
        return

    ordenados = sorted(produto, key=lambda p: p["nome"].lower())

    print(f"  {'ID':<5} {'Nome':<25} {'Categoria':<12} {'Preço':>10} {'Estoque':>8}")
    print("  " + "-" * 65)
    for p in ordenados:
        print(
            f"  {p['id']:<5} {p['nome']:<25} {p['categoria']:<12} "
            f"R$ {p['preco']:>8.2f} {p['estoque']:>8}"
        )
    print("=" * 70)
    print(f"  Total: {len(produto   )} produto(s)")


def buscar_produto_menu():
    """Opção 3 — Busca produto por nome (parcial, case-insensitive)."""
    print("\n" + "=" * 50)
    print("  BUSCAR PRODUTO POR NOME")
    print("=" * 50)

    texto = ler_str("  Digite o nome (ou parte): ")
    resultado = buscar_produtos(produto, texto)

    if not resultado:
        print(f"  Nenhum produto encontrado com '{texto}'.")
        return

    print(f"\n  {len(resultado)} produto(s) encontrado(s):\n")
    print(f"  {'ID':<5} {'Nome':<25} {'Categoria':<12} {'Preço':>10} {'Estoque':>8}")
    print("  " + "-" * 65)
    for p in resultado:
        print(
            f"  {p['id']:<5} {p['nome']:<25} {p['categoria']:<12} "
            f"R$ {p['preco']:>8.2f} {p['estoque']:>8}"
        )


def editar_produto(produto):
    """Bônus — Edita preço e/ou categoria de um produto."""
    print("\n" + "=" * 50)
    print("  EDITAR PRODUTO")
    print("=" * 50)

    if not produto:
        print("  Nenhum produto cadastrado.")
        return

    produto_id = ler_int("  ID do produto a editar: ", minimo=1)
    produto = buscar_produto_por_id(produto, produto_id)

    if not produto:
        print(f"  [!] Produto com ID {produto_id} não encontrado.")
        return

    print(f"\n  Produto: {produto['nome']}")
    print(f"  Categoria atual : {produto['categoria']}")
    print(f"  Preço atual     : R$ {produto['preco']:.2f}")

    print("\n  O que deseja editar?")
    print("  1. Categoria")
    print("  2. Preço")
    print("  3. Ambos")
    print("  0. Cancelar")
    opcao = ler_int("  Opção: ", 0, 3)

    if opcao == 0:
        print("  Edição cancelada.")
        return
    if opcao in (1, 3):
        produto["categoria"] = _escolher_categoria()
    if opcao in (2, 3):
        produto["preco"] = ler_float("  Novo preço (R$): ", minimo=0.0)

    print("  [✓] Produto atualizado.")

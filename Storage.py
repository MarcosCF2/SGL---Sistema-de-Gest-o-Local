import json
import os

ARQUIVO_PRODUTOS = "produtos.json"
ARQUIVO_MOVS = "movs.json"


def carregar_dados():
    """F3 — Carrega os arquivos JSON. Se não existirem, retorna listas vazias."""
    produtos = []
    movs = []

    if os.path.exists(ARQUIVO_PRODUTOS):
        try:
            with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as f:
                produtos = json.load(f)
        except (json.JSONDecodeError, IOError):
            print("  [!] Erro ao carregar produtos.json. Iniciando com lista vazia.")

    if os.path.exists(ARQUIVO_MOVS):
        try:
            with open(ARQUIVO_MOVS, "r", encoding="utf-8") as f:
                movs = json.load(f)
        except (json.JSONDecodeError, IOError):
            print("  [!] Erro ao carregar movs.json. Iniciando com lista vazia.")

    return produtos, movs


def salvar_dados(produtos, movs):
    """F4 — Salva os dados nos arquivos JSON com indent=2."""
    try:
        with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as f:
            json.dump(produtos, f, indent=2, ensure_ascii=False)
        with open(ARQUIVO_MOVS, "w", encoding="utf-8") as f:
            json.dump(movs, f, indent=2, ensure_ascii=False)
        print("  [✓] Dados salvos com sucesso.")
    except IOError as e:
        print(f"  [!] Erro ao salvar dados: {e}")

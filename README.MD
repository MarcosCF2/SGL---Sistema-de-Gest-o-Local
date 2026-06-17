# SGL — Sistema de Gestão Local

Sistema de console em Python para gerenciamento de estoque e movimentações.

---

## Como Executar

**Requisitos:** Python 3.8 ou superior (sem bibliotecas externas).

```bash
# Entre na pasta do projeto
cd sgl

# Execute o sistema
python main.py
```

---

## Estrutura de Arquivos

```
sgl/
├── main.py            # Ponto de entrada — menu principal e loop
├── utils.py           # Funções de leitura e validação (ler_int, ler_float, ler_str)
├── storage.py         # Persistência JSON (carregar_dados, salvar_dados)
├── produtos.py        # Gerenciamento de produtos (cadastrar, listar, buscar, editar)
├── movimentacoes.py   # Registro de entradas e saídas, relatório de movimentações
├── relatorios.py      # Relatório gerencial, exportação TXT, filtro por categoria
├── produtos.json      # Dados persistidos dos produtos
├── movs.json          # Dados persistidos das movimentações
└── README.md          # Este arquivo
```

---

## Funcionalidades

| Opção | Função                                  |
|-------|-----------------------------------------|
| 1     | Cadastrar produto                       |
| 2     | Listar produtos (ordenados por nome)    |
| 3     | Buscar produto por nome (parcial)       |
| 4     | Registrar entrada de estoque            |
| 5     | Registrar saída de estoque              |
| 6     | Relatório de movimentações              |
| 7     | Relatório gerencial (estatísticas)      |
| 8     | Salvar e sair                           |
| B     | **Bônus** — Editar produto              |
| C     | **Bônus** — Filtrar por categoria       |
| E     | **Bônus** — Exportar relatório TXT      |

---

## Casos de Teste

### Caso 1 — Cadastro de produto válido
**Entrada:**
```
Opção: 1
Nome: Feijão Preto 1kg
Categoria: 1 (Alimento)
Preço: 6.50
Estoque: 100
```
**Saída esperada:**
```
[✓] Produto 'Feijão Preto 1kg' cadastrado com ID 6.
```

---

### Caso 2 — Entrada inválida no preço (não numérico)
**Entrada:**
```
Opção: 1
Nome: Teste
Categoria: 5 (Outros)
Preço: abc
Preço: -5
Preço: 10.00
Estoque: 0
```
**Saída esperada:**
```
[!] Entrada inválida. Digite um número válido.
[!] Valor mínimo permitido: 0
[✓] Produto 'Teste' cadastrado com ID X.
```

---

### Caso 3 — Saída bloqueada por estoque insuficiente
**Entrada:**
```
Opção: 5
ID do produto: 3   (Sabonete — estoque 5)
Quantidade: 50
Quantidade: 3
Data: 2026-06-14
Observação: (Enter)
```
**Saída esperada:**
```
[!] Estoque insuficiente! Disponível: 5. Tente novamente.
[✓] Saída registrada. Novo estoque: 2
```

---

### Caso 4 — Busca parcial por nome
**Entrada:**
```
Opção: 3
Texto: det
```
**Saída esperada:**
```
1 produto(s) encontrado(s):
ID   Nome                      Categoria    Preço     Estoque
...  Detergente Líquido 500ml  Limpeza      R$  3.49      28
```

---

### Caso 5 — Relatório gerencial
**Entrada:**
```
Opção: 7
```
**Saída esperada (com dados demo):**
```
[ ESTOQUE MÁXIMO ]
  → Arroz Integral 1kg (ID 1) — 42 unidades

[ ESTOQUE MÍNIMO ]
  → Sabonete Antibacterial (ID 3) — 5 unidades

[ VALOR TOTAL DO ESTOQUE ]
  R$ 2.412,53

[ PRODUTOS POR CATEGORIA ]
  Alimento       : 2 produto(s)
  Eletrônico     : 1 produto(s)
  Higiene        : 1 produto(s)
  Limpeza        : 1 produto(s)

[ TOP 3 — MAIOR VALOR EM ESTOQUE ]
  1. Fone de Ouvido Bluetooth   — R$ 1.499,00
  2. Arroz Integral 1kg         — R$ 377,58
  3. Óleo de Cozinha 900ml      — R$ 140,40
```

---

## Conteúdos Aplicados

- `input/print` com conversões `int/float`
- `if/elif/else` para validações e menu
- `while` para loops de menu e revalidação de entrada
- `for` em listagens e cálculos
- `list` de dicionários para produtos e movimentações
- `str.lower()`, `str.strip()`, `in` para busca parcial
- Funções modulares com parâmetros e retorno
- `json.load / json.dump` para persistência
- `try/except` para tratamento de erros de entrada e I/O

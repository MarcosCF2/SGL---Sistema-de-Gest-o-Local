def ler_int(msg, minimo=None, maximo=None):
    """ F1 - Lè e valida um inteiro com while + try/except. """
    while True:
        try:
            valor = int(input(msg).strip())
            if minimo is not None and valor < minimo:
                print(f"  [!] Valor minimo permitido: {minimo} ")
                continue
            if maximo is not None and valor > maximo:
                print(f"  [!] Valor máximo permitido: {maximo}.")
                continue
            return valor
        except ValueError:  
            print("  [!] Entrada inválida. Digite um número inteiro.")

def ler_float(msg, minimo=None, maximo=None):
    """ F2 - Lè e valida um float com while + try/except. """
    while True:
        try:
            valor = float(input(msg).strip().replace(',', '.'))
            if minimo is not None and valor < minimo:
                print(f"  [!] Valor mínimo permitido: {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"  [!] Valor máximo permitido: {maximo}.")
                continue
            return valor
        except ValueError:  
            print("  [!] Entrada inválida. Digite um número válido.")

def ler_str(msg, obrigatorio=True):
    """Lè uma string, validando se não esta vazia quando orbigtoria. """
    while True:
        valor = input(msg).strip()
        if obrigatorio and not valor: 
            print(f"  [!] Este campo é obrigatório.")
            continue
        return valor

def ler_opcao_menu(minimo=1, maximo=8):
    """Lê e valida a opção de menu principal. """
    return  ler_int(f"\n Escolha uma opção ({minimo}-{maximo}): ", minimo, maximo)
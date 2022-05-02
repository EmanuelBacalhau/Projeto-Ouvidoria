def leiaint(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError ,TypeError):
            print('\033[31mErro: Insira um número válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mErro: Insira um número válido\033[m')
        else:
            return n

def leianome(txt):
    while True:
        try:
            nome = str(input(txt))
        except (ValueError, TypeError):
            print('\033[31mErro: Insira um nome válido\033[m')
        except (KeyboardInterrupt):
            print('\033[31mErro: Insira um nome válido\033[m')
        else:
            return nome

def linha(tamanho=60):
    return '=' * tamanho

def cabecalho(txt):
    print(linha())
    print(txt.center(60))
    print(linha())

def menu(lista):
    c = 1
    for item in lista:
        print(f'\033[33m{c})\033[m \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc

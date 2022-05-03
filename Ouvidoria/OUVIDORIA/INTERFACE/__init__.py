def leiaint(txt): # função criada para ler um número inteiro e validar (tratar erro)
    while True:
        try: # tentar ler o código 
            n = int(input(txt))
        except (ValueError ,TypeError, KeyboardInterrupt): # caso não for o que foi pedido 
            print('\033[31mErro: Insira um número válido\033[m') #imprime
        else: # se der certo código contniua
            return n

def leianome(txt): # função criada para ler str e validar (tratar erro)
    while True:
        try: # tentar ler o código 
            nome = str(input(txt))
        except (ValueError, TypeError, KeyboardInterrupt): # caso não for o que foi pedido 
            print('\033[31mErro: Insira um nome válido\033[m') #imprime
        else: # se der certo código contniua
            return nome

def linha(tamanho=100): # função parar imprimir vários '='
    return '=' * tamanho

def cabecalho(txt): # função para criar um nome e por no meio e entre linhas
    print(linha())
    print(txt.center(100)) # 'center' == meio
    print(linha())

def menu(lista): # função parar formatar menu no código principal e ler sua opção
    c = 1
    for item in lista:
        print(f'\033[33m{c})\033[m \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc

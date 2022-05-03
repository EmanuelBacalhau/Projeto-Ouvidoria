from OUVIDORIA.INTERFACE import * # importar do modulo interface
tipos = ['Sugestão', 'Reclamação', 'Elogios'] 
manifestos = []
sugesotes = []
reclamacoes = []
elogios = []
class OpcsEscondidos(): # criação de classe para por as funções(códigos) do sistema principal
    def opcao1(self, manifestos): # opção 1 == código para por todas manifestações
        if manifestos == []:
            print(f'\033[31m{"Nehuma manifestação encontrada!":^100}\033[m')
        else:
            cont = 1
            for sep in manifestos:
                maniq = sep.replace('#', ' - ')
                print(f'{cont}) Protocolo {maniq}')
                cont += 1
        print(linha())
        return manifestos

    def opcao2(self, manifestos): # opção 2 == codigo para por todas as sugestões
        cont = 1
        if sugesotes == []:
            print(f'\033[31m{"Nenhuma susgestão encontrada!":^100}\033[m')
        for sep in sugesotes:
            maniq = sep.split('#')
            if tipos[0] == maniq[2]:  
                maniq.pop(2)
                print(f'{cont}) PROTOCOLO',end='')
                cont += 1
                for imp in maniq:
                    print(f' - {imp}',end='')
                print()
        print(linha())
        return manifestos
        
    def opcao3(self, manifestos): # opção 3 == código para por todas as reclamações
        cont = 1
        if reclamacoes == []:
             print(f'\033[31m{"Nenhuma reclamação encontrada!":^100}\033[m')
        for sep in reclamacoes:
            maniq2 = sep.split('#')
            if tipos[1] == maniq2[2]:
                maniq2.pop(2)
                print(f'{cont}) PROTOCOLO', end='')
                cont += 1
                for imp in maniq2:
                    print(f' - {imp}', end='')
                print()
        print(linha())
        return manifestos

    def opcao4(self, manifestos): # opção 4 == código para por todos os elogios 
        cont = 1
        if elogios == []:
            print(f'\033[31m{"Nenhum elogio encontrado!":^100}\033[m')
        for sep in elogios:
            maniq3 = sep.split('#')
            if tipos[2] == maniq3[2]:
                maniq3.pop(2)
                print(f'{cont}) PROTOCOLO', end='')
                for imp in maniq3:
                    print(f' - {imp}', end='')
                print()
        print(linha())
        return manifestos

    def opcao5(self, tipos): # opção 5 == código para criar nova manifestação
        opcao = 0
        protocolo = str(len(manifestos) + 1)
        n = leianome('\033[32mRequisitante: \033[m')
        while opc < 1 or opc > 3:
            opc = menu(['1) Sugestão', '2) Reclamação', '3) Elogio']) # menu formatado em no modulo interface
            if opc < 1 or opc > 3:
                print('\033[31mTipo de manifesto inválido!\033[m')
        d = leianome('\033[32mDigite sua descrição: \033[m')
        print(linha())
        manitotal = protocolo + '#' + n + '#' + tipos[opc - 1] + '#' + d
        if opc == 1: # adicionar nas listas
            sugesotes.append(manitotal)
            manifestos.append(manitotal)
        elif opc == 2: # adicionar nas listas
            reclamacoes.append(manitotal)
            manifestos.append(manitotal)
        elif opc == 3: # adicionar nas listas
            elogios.append(manitotal)
            manifestos.append(manitotal)
    
    def opcao6(self, manifestos): # opção 6 == código para pesquisar qualquer manifesto por ID(número)
        cont = 1
        numeroprot = -1
        tamanhoproto = len(manifestos)
        while numeroprot <= 0 or numeroprot > tamanhoproto:
            numeroprot = leiaint('\033[32mInforme o número do protocolo: \033[m') 
            if numeroprot <= 0 or numeroprot > tamanhoproto:
                print('\033[31mNúmero do protolo inválido, consulte-o novamente!\033[m')
                break
        for i in manifestos:
            maniqueb5 = i.split('#')
            if int(maniqueb5[0]) == numeroprot:
                print(f'{cont}) PROTOCOLO', end='')
                for i in  maniqueb5:
                    print(' -', i, end='')
                print()
        print(linha())
                    
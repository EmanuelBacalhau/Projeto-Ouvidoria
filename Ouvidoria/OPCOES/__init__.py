from INTERFACE import *
class Manifescoes:
    tipos = ['Sugestão', 'Reclamação', 'Elogios'] 
    manifest = []
    sugesotes = []
    reclamacoes = []
    elogios = []
class Opcoes:
    def opcao1(self, manifestos): # opção 1 == código para por todas manifestações
        formatar = Formatacao()
        manifestos = Manifescoes()
        if manifestos.manifest == []:
            print(f'\033[31m{"Nehuma manifestação encontrada!":^100}\033[m')
        else:
            cont = 1
            for sep in manifestos.manifest:
                maniq = sep.replace('#', ' - ')
                print(f'{cont}) Protocolo {maniq}')
                cont += 1
        print(formatar.linha())
        return manifestos

    def opcao2(self, manifestos): # opção 2 == codigo para por todas as sugestões
        manifestos = Manifescoes()
        formatar = Formatacao()
        cont = 1
        if manifestos.sugesotes == []:
            print(f'\033[31m{"Nenhuma susgestão encontrada!":^100}\033[m')
        for sep in manifestos.sugesotes:
            maniq = sep.split('#')
            if manifestos.tipos[0] == maniq[2]:  
                maniq.pop(2)
                print(f'{cont}) PROTOCOLO',end='')
                cont += 1
                for imp in maniq:
                    print(f' - {imp}',end='')
                print()
        print(formatar.linha())
        return manifestos
        
    def opcao3(self, manifestos): # opção 3 == código para por todas as reclamações
        manifestos = Manifescoes()
        formatar = Formatacao()
        cont = 1
        if manifestos.reclamacoes == []:
             print(f'\033[31m{"Nenhuma reclamação encontrada!":^100}\033[m')
        for sep in manifestos.reclamacoes:
            maniq2 = sep.split('#')
            if manifestos.tipos[1] == maniq2[2]:
                maniq2.pop(2)
                print(f'{cont}) PROTOCOLO', end='')
                cont += 1
                for imp in maniq2:
                    print(f' - {imp}', end='')
                print()
        print(formatar.linha())
        return manifestos

    def opcao4(self, manifestos): # opção 4 == código para por todos os elogios 
        manifestos = Manifescoes()
        formatar = Formatacao()
        cont = 1
        if manifestos.elogios == []:
            print(f'\033[31m{"Nenhum elogio encontrado!":^100}\033[m')
        for sep in manifestos.elogios:
            maniq3 = sep.split('#')
            if manifestos.tipos[2] == maniq3[2]:
                maniq3.pop(2)
                print(f'{cont}) PROTOCOLO', end='')
                for imp in maniq3:
                    print(f' - {imp}', end='')
                print()
        print(formatar.linha())
        return manifestos

    def opcao5(self, tipos): # opção 5 == código para criar nova manifestação
        manifestos = Manifescoes()
        formatar = Formatacao()
        validar = Validacao()
        opcao = 0
        protocolo = str(len(manifestos.manifest) + 1)
        n = validar.leianome('\033[32mRequisitante: \033[m')
        while opcao < 1 or opcao > 3:
            opcao = formatar.menu(['1) Sugestão', '2) Reclamação', '3) Elogio']) # menu formatado em no modulo interface
            if opcao < 1 or opcao > 3:
                print('\033[31mTipo de manifesto inválido!\033[m')
        d = validar.leianome('\033[32mDigite sua descrição: \033[m')
        print(formatar.linha())
        manitotal = protocolo + '#' + n + '#' + manifestos.tipos[opcao - 1] + '#' + d
        if opcao == 1: # adicionar nas listas
            manifestos.sugesotes.append(manitotal)
            manifestos.manifest.append(manitotal)
        elif opcao == 2: # adicionar nas listas
            manifestos.reclamacoes.append(manitotal)
            manifestos.manifest.append(manitotal)
        elif opcao == 3: # adicionar nas listas
            manifestos.elogios.append(manitotal)
            manifestos.manifest.append(manitotal)
    
    def opcao6(self, manifestos): # opção 6 == código para pesquisar qualquer manifesto por ID(número)
        formatar = Formatacao()
        validar = Validacao()
        manifestos = Manifescoes()
        cont = 1
        numeroprot = -1
        tamanhoproto = len(manifestos.manifest)
        while numeroprot <= 0 or numeroprot > tamanhoproto:
            numeroprot = validar.leiaint('\033[32mInforme o número do protocolo: \033[m') 
            if numeroprot <= 0 or numeroprot > tamanhoproto:
                print('\033[31mNúmero do protolo inválido, consulte-o novamente!\033[m')
                break
        for i in manifestos.manifest:
            maniqueb5 = i.split('#')
            if int(maniqueb5[0]) == numeroprot:
                print(f'{cont}) PROTOCOLO', end='')
                for i in  maniqueb5:
                    print(' -', i, end='')
                print()
        print(formatar.linha())
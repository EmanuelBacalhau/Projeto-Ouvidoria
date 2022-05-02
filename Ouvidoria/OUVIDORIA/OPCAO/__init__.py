from OUVIDORIA.INTERFACE import *
tipos = ['Sugestão', 'Reclamação', 'Elogios']
manifestos = []
sugesotes = []
reclamacoes = []
elogios = []
class OpcsEscondidos():
    def opc1(self, manifestos):
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

    def opc2(self, manifestos):
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
        
    def opc3(self, manifestos):
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

    def opc4(self, manifestos):
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

    def opc5(self, tipos):
        opc = 0
        prot = str(len(manifestos) + 1)
        n = leianome('\033[32mRequisitante: \033[m')
        while opc < 1 or opc > 3:
            print('1) Sugestão')
            print('2) Reclamação')
            print('3) Elogio')
            opc = leiaint('\033[32mQual o tipo do seu manifesto: \033[m')
            if opc < 1 or opc > 3:
                print('\033[31mTipo de manifesto inválido!\033[m')
        d = leianome('\033[32mDigite sua descrição: \033[m')
        print(linha())
        manitotal = prot + '#' + n + '#' + tipos[opc - 1] + '#' + d
        if opc == 1:
            sugesotes.append(manitotal)
            manifestos.append(manitotal)
        elif opc == 2:
            reclamacoes.append(manitotal)
            manifestos.append(manitotal)
        elif opc == 3:
            elogios.append(manitotal)
            manifestos.append(manitotal)
    
    def opc6(self, manifestos):
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
                    
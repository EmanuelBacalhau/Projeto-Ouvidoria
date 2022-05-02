from OUVIDORIA.INTERFACE import *
manifestos = []
tipos = ['Sugestão', 'Reclamação', 'Elogios']
class OpcsEscondidos():
    def opc1(self, manifestos):
        if manifestos == []:
            print(f'\033[31m{"Nehuma manifestação encontrada!":^60}\033[m')
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
        for sep in manifestos:
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
        for sep in manifestos:
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
        for sep in manifestos:
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
        manifestos.append(manitotal)
    
    def opc6(self, manifestos):
        cont = 1
        protn = 0
        tam = len(manifestos)
        if manifestos == []:
            print(f'\033[31m{"Nehum protocolo encontrado!":^60}\033[m')
            print(linha())
        else:
            protn = leiaint('\033[32mDigite o número do seu protocolo: \033[m')
            if protn > tam or protn < tam:
                print('\033[31mProtocolo não encontrado, consulte-o novamente!\033[m')
            else:
                for sep in manifestos:
                    maniq4 = sep.split('#')
                    if int(maniq4[0]) == protn:
                        print(f'{cont}) PROTOCOLO', end='')
                        cont += 1
                        for imp in maniq4:
                            print(f' - {imp}', end='')
                        print()
                print(linha())
                    
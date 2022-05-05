from Atalhos import *
validar = Validacao()
formatar = Formatacao()
opcao = 0 
manifestos = []
tipos = 'Sugestão', 'Reclamação', 'Elogio'
formatar.cabecalho('OUVIDORIA ABC')
while True:
    opcao = formatar.menu(['Listar todas as manifestações', 'Listar todas as sugestões', 'Listar todas as reclamações', 'Listar todas os elogios', 'Criar nova manifestação', 'Pesquisar por protocolo por ID', 'Sair'])
    if opcao == 1: #Mostrar todas as manifestações disponíveis.
        formatar.cabecalho('Manifestações:')
        for i in manifestos:
            maniqueb = i.replace('#', ' - ')
            print('Procolo', maniqueb)
        print(formatar.linha())
    elif opcao == 2: #Mostrar sugestões as disponiveís.
        formatar.cabecalho('Sugestões:')
        for i in manifestos:
            maniqueb2 = i.split('#')
            if tipos[0] == maniqueb2[2]: #Se os tipos[0] for igua a maniqueb2(manifestos quebrado) imprime as sugestões.
                maniqueb2.pop(2)
                print('Procolo', end='')
                for i in maniqueb2:
                    print(' -', i, end='')
        print()
        print(formatar.linha())

    elif opcao == 3: #Mostrar todas as reclamações.
        formatar.cabecalho('Reclamações:')
        for i in manifestos:
            maniqueb3 = i.split('#')
            if tipos[1] == maniqueb3[2]: #Se os tipos[1] for igua a maniqueb3(manifestos quebrado) imprime as reclamações.
                maniqueb3.pop(2)
                print('Procolo', end='')
                for i in maniqueb3:
                    print(' -', i, end='')
        print()
        print(formatar.linha())
    elif opcao == 4: #Mostrar todos os elogios.
        formatar.cabecalho('Elogios:')
        for i in manifestos:
            maniqueb4 = i.split('#')
            if tipos[2] == maniqueb4[2]: #Se os tipos[2] for igua a maniqueb4(manifestos quebrado) imprime os elogios.
                maniqueb4.pop(2)
                print('Procolo', end='')
                for i in maniqueb4:
                    print(' -', i, end='')    
        print()
        print(formatar.linha())    
    elif opcao == 5: #Enviar nova manifestação conforme seu tipo.
        tipo = 0
        prot = str(len(manifestos) + 1)
        nome = validar.leianome('Requisitante: ')
        while tipo < 1 or tipo > 3:
            tipo = formatar.menu(['Sugestão', 'Reclamação', 'Elogio'])
            if tipo < 1 or tipo > 3: #Menor que 1 ou maiores que 3 ==> Opção inválida.
                print('Opção inválida!')
        descricao = validar.leianome('Digite seu manifesto: ')
        print(formatar.linha())
        manifestostotal = prot + '#' + nome + '#' + tipos[tipo-1] + '#' + descricao
        manifestos.append(manifestostotal) #Adicionar dentro de manifestos.
    elif opcao == 6: #Pesquisar manifetações por número(ID).
        numeroprot = -1
        tamanhoproto = len(manifestos)
        while numeroprot <= 0 or numeroprot > tamanhoproto:
            numeroprot = validar.leiaint('Informe o número do protocolo: ') #Pesquisar manifestação por número.
            if numeroprot <= 0 or numeroprot > tamanhoproto: #Menor ou igual 0, ou maior que o tamanho do protocolo imprime o print.
                print('Número do protolo inválido, consulte-o novamente!')
                break
        for i in manifestos:
            maniqueb5 = i.split('#') #Manifestos quebrado.
            if int(maniqueb5[0]) == numeroprot: #Se maniqueb5[0] for igual ao numeroprot imprime a manifestação.
                print('Procolo', end='')
                for i in  maniqueb5:
                    print(' -', i, end='')
                print()
        print(formatar.linha())
     
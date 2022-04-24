opcao = 0 
manifestos = []
tipos = ['Sugestão', 'Reclamação', 'Elogio']
print('='*35)
print('{:^45}'.format('\033[1;94mOUVIDORIA ABC\033[m')) #Colocar no meio
while opcao !=7:
    print('='*35)
    print('1) Listar todas as manifestações.')
    print('2) Listar todas as sugestões.')
    print('3) Listar todas as reclamações.')
    print('4) Listar todas os elogios.')
    print('5) Enviar nova manifestação.')
    print('6) Pesquisar por protocolo por ID.')
    print('7) Sair')
    print('='*35)
    opcao = int(input('\033[1;94mDigite a opção que você deseja: \033[m'))
    print()
    if opcao < 1 or opcao > 7: #Menor que 1 ou maiores que 7 ==> Opção inválida.
        print('\033[1;31mOpção inválida!\033[m')

    elif opcao == 1: #Mostrar todas as manifestações disponíveis.
        print('\033[1;94mManifestações:\033[m')
        if manifestos == []: #Se manifestor for igual [] imprime o print.
            print('\033[1;31mNenhuma manifestação encontrada!\033[m')
        for i in manifestos:
            maniqueb = i.replace('#', ' - ')
            print('CÓDIGO', maniqueb)

    elif opcao == 2: #Mostrar sugestões as disponiveís.
        print('\033[1;94mSugestões:\033[m')
        for i in manifestos:
            maniqueb2 = i.split('#')
            if tipos[0] == maniqueb2[2]: #Se os tipos[0] for igua a maniqueb2(manifestos quebrado) imprime as sugestões.
                maniqueb2.pop(2)
                print('CÓDIGO', end='')
                for i in maniqueb2:
                    print(' -', i, end='')
            print()

    elif opcao == 3: #Mostrar todas as reclamações.
        print('\033[1;94mReclamações:\033[m')
        for i in manifestos:
            maniqueb3 = i.split('#')
            if tipos[1] == maniqueb3[2]: #Se os tipos[1] for igua a maniqueb3(manifestos quebrado) imprime as reclamações.
                maniqueb3.pop(2)
                print('CÓDIGO', end='')
                for i in maniqueb3:
                    print(' -', i, end='')
            print()

    elif opcao == 4: #Mostrar todos os elogios.
        print('\033[1;94mElogios:\033[m')
        for i in manifestos:
            maniqueb4 = i.split('#')
            if tipos[2] == maniqueb4[2]: #Se os tipos[2] for igua a maniqueb4(manifestos quebrado) imprime os elogios.
                maniqueb4.pop(2)
                print('CÓDIGO', end='')
                for i in maniqueb4:
                    print(' -', i, end='')    
            print()
            
    elif opcao == 5: #Enviar nova manifestação conforme seu tipo.
        tipo = 0
        prot = str(len(manifestos) + 1)
        nome = str(input('\033[1;94mRequisitante: \033[m'))
        while tipo < 1 or tipo > 3:
            print('1) Sugestão')
            print('2) Reclamação')
            print('3) Elogio ')
            tipo = int(input('\033[1;94mDigite o tipo de manifestação: \033[m'))
            if tipo < 1 or tipo > 3: #Menor que 1 ou maiores que 3 ==> Opção inválida.
                print('\033[1;31mOpção inválida!\033[m')
        descricao = str(input('\033[1;94mDigite seu manifesto: \033[m'))
        manifestostotal = prot + '#' + nome + '#' + tipos[tipo-1] + '#' + descricao
        manifestos.append(manifestostotal) #Adicionar dentro de manifestos.

    elif opcao == 6: #Pesquisar manifetações por número(ID).
        numeroprot = -1
        tamanhoproto = len(manifestos)
        while numeroprot <= 0 or numeroprot > tamanhoproto:
            numeroprot = int(input('\033[1;34mInforme o número do protocolo: \033[m')) #Pesquisar manifestação por número.
            if numeroprot <= 0 or numeroprot > tamanhoproto: #Menor ou igual 0, ou maior que o tamanho do protocolo imprime o print.
                print('\033[1;31mNúmero do protolo inválido, consulte-o novamente!\033[m')
                break
        for i in manifestos:
            maniqueb5 = i.split('#') #Manifestos quebrado.
            if int(maniqueb5[0]) == numeroprot: #Se maniqueb5[0] for igual ao numeroprot imprime a manifestação.
                print('CÓDIGO', end='')
                for i in  maniqueb5:
                    print(' -', i, end='')
     
print('\033[1;31mSaindo... Volte sempre!\033[m')
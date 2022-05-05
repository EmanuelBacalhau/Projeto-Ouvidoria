from INTERFACE import *
from OPCOES import *
validar = Validacao()
formatar = Formatacao()
manifestos = Manifescoes()
OPcao = Opcoes()
formatar.cabecalho('OUVIDORIA ABC')
while True:
    resp = formatar.menu(['Listar todas manifestações', 'Listar todas as sugestões', 'Listar todas as reclamações', 'Listar todos elogios', 'Criar novo manifesto', 'Pesquisar protcolo por ID', 'Sair'])
    if resp == 1:
        formatar.cabecalho('Manifestações: ')
        OPcao.opcao1(manifestos)
    elif resp == 2:
        formatar.cabecalho('Sugestões: ') 
        OPcao.opcao2(manifestos)
    elif resp == 3:
        formatar.cabecalho('Reclamações: ') 
        OPcao.opcao3(manifestos)
    elif resp == 4:
        formatar.cabecalho('Elogios: ') 
        OPcao.opcao4(manifestos)
    elif resp == 5:
        formatar.cabecalho('Novo manifesto: ') 
        OPcao.opcao5(manifestos)
    elif resp == 6:
        formatar.cabecalho('Pesquisar protocolo por ID: ') 
        OPcao.opcao6(manifestos)
    elif resp == 7:
        print('Saindo... Até logo!')
        break
    else:
        print('\033[31mErro: Opção inválida!\033[m')
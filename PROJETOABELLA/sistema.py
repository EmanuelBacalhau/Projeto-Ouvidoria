from OUVIDORIA.INTERFACE import *
from OUVIDORIA.OPCAO import *
cabecalho('OUVIDORIA ABC')
while True:
    ops = OpcsEscondidos()
    resp = menu(['Listar todas manifestações', 'Listar todas sugestções', 'Listar todas reclamações',
    'Listar todos elogios', 'Enviar nova manifestação', 'Pesquisar manifestação pelo protocolo', 'Sair'])
    if resp == 1:
      cabecalho('Manifestação: ')
      ops.opc1(manifestos) 
    elif resp == 2:
      cabecalho('Sugestões: ')
      ops.opc2(manifestos)
    elif resp == 3:
      cabecalho('Reclamações:')
      ops.opc3(manifestos)
    elif resp == 4:
      cabecalho('Elogios: ')
      ops.opc4(manifestos)
    elif resp == 5:
      cabecalho('Novo Manifesto: ')
      ops.opc5(tipos)
    elif resp == 6:
      cabecalho('Procolos: ')
      ops.opc6(manifestos)
    elif resp == 7:
      cabecalho('Saindo... Até logo!')
      break
    else:
      print('\033[31mErro: Digite uma opção válida!\033[m')
      print(linha())
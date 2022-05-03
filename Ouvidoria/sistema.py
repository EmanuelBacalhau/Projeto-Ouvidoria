from OUVIDORIA.INTERFACE import * #Importar funções  
from OUVIDORIA.OPCAO import * #Importar funções
cabecalho('OUVIDORIA ABC') #'cabecalho' função importada da ouvidoria interface
while True:
    opcoes = OpcsEscondidos() # classe importada de OPCAO
    resp = menu(['Listar todas manifestações', 'Listar todas sugestões', 'Listar todas reclamações', #menu formatado 
    'Listar todos elogios', 'Criar nova manifestação', 'Pesquisar manifestação pelo protocolo', 'Sair'])
    if resp == 1: #1 listar todas manifestações
      cabecalho('Manifestação: ')
      opcoes.opcao1(manifestos) #classe e função importada de OPCAO
    elif resp == 2: #2 listar todas sugestões
      cabecalho('Sugestões: ')
      opcoes.opcao2(manifestos)
    elif resp == 3: #3 listar todas reclamações
      cabecalho('Reclamações:')
      opcoes.opcao3(manifestos)
    elif resp == 4: # listar todos elogios
      cabecalho('Elogios: ')
      opcoes.opcao4(manifestos)
    elif resp == 5: # Criar nova manifestação
      cabecalho('Novo Manifesto: ')
      opcoes.opcao5(tipos)
    elif resp == 6: # Procurar manifestação por número 
      cabecalho('Protocolos: ')
      opcoes.opcao6(manifestos)
    elif resp == 7: # Sair
      cabecalho('Saindo... Até logo!')
      break
    else: # Caso digite algum número maior 7 ou menor que 1 == erro
      print('\033[31mErro: Digite uma opção válida!\033[m')
      print(linha())
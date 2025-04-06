from operacoesbd import *
 
conexao = criarConexao("localhost", "rote", "19042005", "ouvidoria")
opcao = 0
while opcao != 5:
    print("escolha uma das opçoes abaixo:"
    "\n1 - listagem de manifestações"
    "\n2 - Listagem de manifestações por tipo"
    "\n3 - criar uma nova manifestação"
    "\n4 - exibir quantidade de manifestações"
    "\n5 pesquisar uma manisfestação por codigo"
    "\n6 - Excluir manifestação pelo código"
    "\n7 - Sair do Sistema")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        listarManifestações = "SELECT * FROM manifestacao"
        listagem = listarBancoDados(conexao, listarManifestações)
        if len(listagem) == 0:
            print("Não há manifestações cadastradas")
        else:       
            print("lista de manifestações")
            contagem = 0
            for manifestacao in listagem:
                contagem += 1
                print(contagem, manifestacao[0])
    elif opcao == 2:
        tipo = input("Digite o tipo de manifestação: reclamação, elogio ou sugestão: ")
        if tipo not in ["reclamação", "elogio", "sugestão"]:
            print("Tipo inválido")
            continue
        dados = [tipo]
        listarManifestaçõesTipo = "SELECT * FROM manifestacao WHERE tipo = %s"
        listagem = listarBancoDados(conexao, listarManifestaçõesTipo, dados)
        if len(listagem) == 0:
            print("Não há manifestações cadastradas desse tipo")
        else:       
            print("lista de manifestações tipo:", tipo)
            contagem = 0
            for manifestacao in listagem:
                contagem += 1
                print(contagem, manifestacao[0])
    elif opcao == 3:
    


    elif opcao == 7:
        print("Saindo...")
        encerrarConexao(conexao)
    else:
        print("Opção inválida")
        
    
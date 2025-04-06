from operacoesbd import *
 
conexao = criarConexao("localhost", "root", "19042005", "ouvidoria")
opcao = 0
while opcao != 7:
    print("escolha uma das opçoes abaixo:"
    "\n1 - listagem de manifestações"
    "\n2 - Listagem de manifestações por tipo"
    "\n3 - criar uma nova manifestação"
    "\n4 - exibir quantidade de manifestações"
    "\n5 - pesquisar uma manisfestação por codigo"
    "\n6 - Excluir manifestação pelo código"
    "\n7 - Sair do Sistema")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        listarManifestações = "SELECT * FROM manifestacoes"
        listagem = listarBancoDados(conexao, listarManifestações)
        if len(listagem) <= 0:
            print("Não há manifestações cadastradas")
        else:       
            print("lista de manifestações")
            contagem = 0
            for manifestacao in listagem:
                contagem += 1
                print(f"{contagem} - Nome: {manifestacao[0]} | Tipo: {manifestacao[1]} | Código: {manifestacao[2]} | Manifestação: {manifestacao[3]}")
    elif opcao == 2:
        tipo = input("Digite o tipo de manifestação: reclamação, elogio ou sugestão: ")
        if tipo not in ["reclamação", "elogio", "sugestão"]:
            print("Tipo inválido")
            continue
        dados = [tipo]
        listarManifestaçõesTipo = "SELECT * FROM manifestacoes WHERE tipo = %s"
        listagem = listarBancoDados(conexao, listarManifestaçõesTipo, dados)
        if len(listagem) == 0:
            print("Não há manifestações cadastradas desse tipo")
        else:       
            print("lista de manifestações tipo:", tipo)
            contagem = 0
            for manifestacao in listagem:
                contagem += 1
                print(f"{contagem} - Nome: {manifestacao[0]} | Tipo: {manifestacao[1]} | Código: {manifestacao[2]} | Manifestação: {manifestacao[3]}")
    elif opcao == 3:
        nome = input("Digite o nome do usuário: ")
        tipo = input("Digite o tipo de manifestação: reclamação, elogio ou sugestão: ")
        manifestacao = input("Digite a manifestação: ")
        if tipo not in ["reclamação", "elogio", "sugestão"]:
            print("Tipo inválido")
            continue
        dados = [nome, tipo, manifestacao]
        inserirManifestacao = "INSERT INTO manifestacoes (nome, tipo, manifestaçao) VALUES (%s, %s, %s)"
        insertNoBancoDados(conexao, inserirManifestacao, dados)
        print("Manifestação cadastrada com sucesso")
    elif opcao == 4:
        listarContagem = "SELECT COUNT(*) FROM manifestacoes"
        contagem = listarBancoDados(conexao, listarContagem)
        print("Total de manifestações cadastradas:", contagem[0][0])
    elif opcao == 5:
        codigo = int(input("Digite o código da manifestação: "))
        dados = [codigo]
        listarManifestacaoCodigo = "SELECT * FROM manifestacoes WHERE codigo = %s"
        listagem = listarBancoDados(conexao, listarManifestacaoCodigo, dados)
        if len(listagem) == 0:
            print("Não há manifestação cadastrada com esse código")
        else:       
            print("manifestação encontrada")
            for manifestacao in listagem:
               print(f"""
    -------------------------------
    Código:         {manifestacao[2]}
    Nome:           {manifestacao[0]}
    Tipo:           {manifestacao[1]}
    Manifestação:   {manifestacao[3]}
    -------------------------------
    """)

    elif opcao == 6:
        codigo = int(input("Digite o código da manifestação que deseja excluir: "))
        dados = [codigo]
        excluirManifestacao = "DELETE FROM manifestacoes WHERE codigo = %s"
        linhasAfetadas = excluirBancoDados(conexao, excluirManifestacao, dados)
        if linhasAfetadas > 0:
            print("Manifestação excluída com sucesso")
        else:
            print("Não há manifestaçõe cadastrada com esse código")
    elif opcao == 7:
        print("Saindo...")
        encerrarConexao(conexao)
    else:
        print("Opção inválida")
        
    
# imports e constantes globais
import csv
import os
import getpass

usuariosFile = 'usuarios.csv'
produtosFile = 'produtos.csv'

# FUNÇÕES DE GERENCIAMENTOS DE DADOS


def carregarDados(caminhoArquivo):
    dados = []
    cabecalho = []
    if not os.path.exists(caminhoArquivo):
        # define cabecalhos se o arquivo não existir
        if 'usuarios' in caminhoArquivo:
            cabecalho = ['idUsuario', 'username', 'password', 'role']
        elif 'produtos' in caminhoArquivo:
            cabecalho = ['idProduto', 'nome', 'preco', 'quantidade']

        with open(caminhoArquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(cabecalho)
        return dados

    with open(caminhoArquivo, mode='r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            dados.append(linha)
    return dados


def salvaDados(caminhoArquivo, dados):
    # salva uma lista de dicionários em um arquivo CSV
    if not dados:
        return

    cabecalho = dados[0].keys()
    with open(caminhoArquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)
        escritor.writeheader()
        escritor.writerows(dados)


def obterProximoID(dados, chaveID):
    # calcula o próximo ID disponível
    if not dados:
        return 1
    return max(int(d[chaveID]) for d in dados) + 1

# FUNÇÕES DE GERENCIAMENTOS DE USUÁRIOS


def criarUsuario(listaUsuarios):
    # cria um novo usuário e o adiciona na lista
    print('\nCadastro de Novo Usuário')
    username = input('Nome de usuário: ')
    for u in listaUsuarios:
        if u['username'] == username:
            print('ERRO: Nome de usuário já existe.')
            return

    password = input('Senha: ')
    role = ''
    while role not in ['admin', 'funcionario']:
        role = input('Permissão (admin/funcionario): ').lower()
        if role not in ['admin', 'funcionario']:
            print('Permissão inválida. Tente novamente.')

    novoID = obterProximoID(listaUsuarios, 'idUsuario')
    novoUsuario = {
        'idUsuario': novoID,
        'username': username,
        'password': password,
        'role': role
    }
    listaUsuarios.append(novoUsuario)
    print('Usuário cadastrado com sucesso!')


def listarUsuarios(listaUsuarios):
    # lista todos os usuários cadastrados
    print('\nLista de usuários')
    if not listaUsuarios:
        print('Nenhum usuário cadastrado.')
        return

    print(f"{'ID':<5} {'Username':<20} {'Role':<15}")
    print('-' * 40)

    for usuario in listaUsuarios:
        print(
            f"{usuario['idUsuario']:<5} {usuario['username']:<20} {usuario['role']:<15}")


def atualizarUsuario(listaUsuarios):
    # atualiza os dados de um usuário existente.
    print('\nAtualizar usuário')
    idUsuario = input('Digite o ID do usuário que deseja atualizar: ')

    usuarioEncontrado = None
    for usuario in listaUsuarios:
        if usuario['idUsuario'] == idUsuario:
            usuarioEncontrado = usuario
            break

    if not usuarioEncontrado:
        print('Usuário não encontrado.')
        return

    print(f"Atualizando usuário: {usuarioEncontrado['username']}")
    novoUsername = input(
        f"Novo nome de usuário (deixe em branco para manter '{usuarioEncontrado['username']}'): ")
    novaSenha = input("Nova senha (deixe em branco para não alterar): ")
    novoRole = input(
        f"Nova permissão (admin/funcionario, deixe em branco para manter '{usuarioEncontrado['role']}'): ").lower()

    if novoUsername:
        for u in listaUsuarios:
            if u['username'] == novoUsername and u['idUsuario'] != idUsuario:
                print('ERRO: Novo nome de usuário já está em uso.')
                return
        usuarioEncontrado['username'] = novoUsername

    if novaSenha:
        usuarioEncontrado['password'] = novaSenha
    if novoRole and novoRole in ['admin', 'funcionario']:
        usuarioEncontrado['role'] = novoRole
    elif novoRole:
        print("Permissão inválida. A permissão não foi alterada.")

    print("Usuário atualizado com sucesso!")


def deletarUsuario(listaUsuarios):
    # Remove um usuário da lista
    print('\nDeletar usuário')
    idUsuario = input("Digite o ID do usuário que deseja deletar: ")

    usuarioINDEX = -1
    for i, usuario in enumerate(listaUsuarios):
        if usuario['idUsuario'] == idUsuario:
            if usuario['role'] == 'admin':
                print('ERRO: Não é possível deletar um usuário administrador.')
                return
            usuarioINDEX = i
            break

    if usuarioINDEX != -1:
        del listaUsuarios[usuarioINDEX]
        print("Usuário deletado com sucesso!")
    else:
        print("Usuário não encontrado.")

# FUNÇÕES DE GERENCIAMENTO DE PRODUTOS


def criarProdutos(listaProdutos):
    # cria um novo produto
    print('\nCadastro de novo produto')
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: '))
    quantidade = int(input('Quantidade em estoque: '))

    novoID = obterProximoID(listaProdutos, 'idProduto')
    novoProduto = {'idProduto': novoID, 'nome': nome,
                   'preco': preco, 'quantidade': quantidade}

    listaProdutos.append(novoProduto)
    print('Produto cadastrado com sucesso!')


def listarProdutos(listaProdutos, titulo='Lista de produtos'):
    # lista todos os produtos
    print(f'\n{titulo}')
    if not listaProdutos:
        print('Nenhum produto encontrado.')
        return

    print(f"{'ID':<5} {'Nome':<30} {'Preço (R$)':<15} {'Quantidade':<10}")
    print("-" * 65)

    for produto in listaProdutos:
        precoFormatado = f"{float(produto['preco']):.2f}"
        print(
            f"{produto['idProduto']:<5} {produto['nome']:<30} {precoFormatado:<15} {produto['quantidade']:<10}")


def atualizarProduto(listaProdutos, usuarioLogado):
    # atualiza os dados de um produto
    print('\nAtualizar produto')
    idProduto = input('Digite o ID do produto que deseja atualizar: ')

    produtoEncontrado = None
    for produto in listaProdutos:
        if produto['idProduto'] == idProduto:
            produtoEncontrado = produto
            break

    if not produtoEncontrado:
        print("Produto não encontrado.")
        return

    print(f"Atualizando produto: {produtoEncontrado['nome']}")

    if usuarioLogado['role'] == 'admin':
        novoNome = input(
            f"Novo nome (deixe em branco para manter '{produtoEncontrado['nome']}'): ")
        novoPrecoSTR = input(
            f"Novo preço (deixe em branco para manter '{produtoEncontrado['preco']}'): ")
        if novoNome:
            produtoEncontrado['nome'] = novoNome
        if novoPrecoSTR:
            produtoEncontrado['preco'] = float(novoPrecoSTR)

    novaQuantidadeSTR = input(
        f"Nova quantidade (deixe em branco para manter '{produtoEncontrado['quantidade']}'): ")
    if novaQuantidadeSTR:
        produtoEncontrado['quantidade'] = int(novaQuantidadeSTR)
    print('Produto atualizado com sucesso!')


def deletarProduto(listaProdutos):
    # remove um produto da lista
    print('\nDeletar produto')
    idProduto = input('Digite o ID do produto que deseja deletar: ')

    produtoINDEX = -1
    for i, produto in enumerate(listaProdutos):
        if produto['idProduto'] == idProduto:
            produtoINDEX = i
            break

    if produtoINDEX != -1:
        del listaProdutos[produtoINDEX]
        print("Produto deletado com sucesso!")
    else:
        print("Produto não encontrado.")


def buscarProdutoPorNome(listaProdutos):
    # busca produtos cujo nome contém o termo pesquisado
    print('\nBuscar produto por nome')
    termoBusca = input('Digite o nome ou parte do nome do produto: ').lower()

    resultados = []
    for produto in listaProdutos:
        if termoBusca in produto['nome'].lower():
            resultados.append(produto)

    if resultados:
        listarProdutos(resultados, titulo='Resultados da busca')
    else:
        print("Nenhum produto encontrado com este termo.")


def imprimirOrdenadoPorNome(listaProdutos):
    # imprime a lista de produtos ordenada por nome
    produtosOrdenados = sorted(listaProdutos, key=lambda p: p['nome'].lower())
    listarProdutos(produtosOrdenados, titulo='Produtos ordenados por nome')


def imprimirOrdenadoPorPreco(listaProdutos):
    # imprime a lista de produtos ordenada por preço
    produtosOrdenados = sorted(listaProdutos, key=lambda p: float(p['preco']))
    listarProdutos(produtosOrdenados, titulo="Produtos Ordenados por Preço")


# FUNÇÕES DE INTERFACE DE USUÁRIO E SESSÃO

def limparTela():
    # limpa o console para melhorar a legibilidade
    os.system('cls' if os.name == 'nt' else 'clear')


def exibirMenuInicial():
    # exibe o menu principal da loja
    print("\n" + "="*30)
    print("   Sistema de Brincadeirinha!   ")
    print("="*30)
    print("Escolha uma das opções abaixo:")
    print("1. Fazer Login")
    print("2. Sair do sistema")
    return input("Digite o número da opção desejada [1/2]: ")


def exibirMenuAdmin(nomeUsuario):
    # exibe o menu para administradores
    print(f"\n--- Menu Interno (Admin) ---\nOlá {nomeUsuario}!")
    print("Escolha uma das opções abaixo:\n")
    print("--- Gerenciar Produtos ---")
    print("1. Listar todos os produtos")
    print("2. Cadastrar novo produto")
    print("3. Atualizar produto")
    print("4. Deletar produto")
    print("5. Buscar produto por nome")
    print("6. Imprimir produtos ordenados por nome")
    print("7. Imprimir produtos ordenados por preço")
    print("\n--- Gerenciar Usuários ---")
    print("8. Listar todos os usuários")
    print("9. Cadastrar novo usuário")
    print("10. Atualizar usuário")
    print("11. Deletar usuário")
    print("\nPara fazer logout digite 0")
    return input("Digite o número da opção desejada: ")


def exibirMenuFuncionario(nomeUsuario):
    # exibe menu para funcionários
    print(f"\n--- Menu Interno (Funcionário) ---\nOlá {nomeUsuario}!")
    print("Escolha uma das opções abaixo:\n")
    print("1. Listar todos os produtos")
    print("2. Atualizar quantidade de produto")
    print("3. Buscar produto por nome")
    print("4. Imprimir produtos ordenados por nome")
    print("5. Imprimir produtos ordenados por preço")
    print("\nPara fazer logout digite 0")
    return input("Digite o número da opção desejada: ")


def login(listaUsuarios):
    # realiza processo de autenticação
    print("\n--- Tela de Login ---")
    print("Por favor, insira suas credenciais.")
    username = input("Nome de Usuário: ")
    password = getpass.getpass("Senha: ")

    for usuario in listaUsuarios:
        if usuario['username'] == username and usuario['password'] == password:
            print("\nLogin bem-sucedido!")
            return usuario
    print("\nLogin falhou! Nome de usuário ou senha incorretos.")
    return None


# BLOCO DE EXECUÇÃO PRINCIPAL

usuarios = carregarDados(usuariosFile)
produtos = carregarDados(produtosFile)

while True:
    limparTela()
    opcaoInicial = exibirMenuInicial()

    if opcaoInicial == '1':
        usuarioLogado = login(usuarios)

        if usuarioLogado:
            while True:
                limparTela()
                if usuarioLogado['role'] == 'admin':
                    opcaoInterna = exibirMenuAdmin(usuarioLogado['username'])
                    if opcaoInterna == '1':
                        listarProdutos(produtos)
                    elif opcaoInterna == '2':
                        criarProdutos(produtos)
                        salvaDados(produtosFile, produtos)
                    elif opcaoInterna == '3':
                        atualizarProduto(produtos, usuarioLogado)
                        salvaDados(produtosFile, produtos)
                    elif opcaoInterna == '4':
                        deletarProduto(produtos)
                        salvaDados(produtosFile, produtos)
                    elif opcaoInterna == '5':
                        buscarProdutoPorNome(produtos)
                    elif opcaoInterna == '6':
                        imprimirOrdenadoPorNome(produtos)
                    elif opcaoInterna == '7':
                        imprimirOrdenadoPorPreco(produtos)
                    elif opcaoInterna == '8':
                        listarUsuarios(usuarios)
                    elif opcaoInterna == '9':
                        criarUsuario(usuarios)
                        salvaDados(usuariosFile, usuarios)
                    elif opcaoInterna == '10':
                        atualizarUsuario(usuarios)
                        salvaDados(usuariosFile, usuarios)
                    elif opcaoInterna == '11':
                        deletarUsuario(usuarios)
                        salvaDados(usuariosFile, usuarios)
                    elif opcaoInterna == '0':
                        break
                    else:
                        print("Opção inválida.")

                elif usuarioLogado['role'] == 'funcionario':
                    opcaoInterna = exibirMenuFuncionario(
                        usuarioLogado['username'])
                    if opcaoInterna == '1':
                        listarProdutos(produtos)
                    elif opcaoInterna == '2':
                        atualizarProduto(produtos, usuarioLogado)
                        salvaDados(produtosFile, produtos)
                    elif opcaoInterna == '3':
                        buscarProdutoPorNome(produtos)
                    elif opcaoInterna == '4':
                        imprimirOrdenadoPorNome(produtos)
                    elif opcaoInterna == '5':
                        imprimirOrdenadoPorPreco(produtos)
                    elif opcaoInterna == '0':
                        break
                    else:
                        print("Opção inválida.")

                input("\nPressione Enter para continuar...")

    elif opcaoInicial == '2':
        print("Sistema encerrado. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
        input("Pressione Enter para continuar...")

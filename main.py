from operacoes import *
from banco import *

def menu():
    while True:
        print("---- BEM VINDO AO MENU ----")
        print("1 - adicionar conta")
        print("2 - editar nome")
        print("3 - excluir conta")
        print("4 - consultar conta")
        print("5 - listar todas as contas")
        print("6 - consultar saldo")
        print("7 - fazer depósito")
        print("8 - fazer saque")
        print("9 - transferência")
        print("10 - sair")
        opcao = int(input('selecione uma opção: '))

        if opcao == 1:
            nome = input('Digite o nome do cliente: ')
            saldo = float(input('digite o saldo: '))
            adicionarConta(nome,saldo)
        elif opcao == 2:
            conta = int(input('Digite o número da conta: '))
            novoNome = input('Digite o novo nome: ')
            editarNome(novoNome, conta)
        elif opcao == 3:
            conta = int(input('Digite o número da conta: '))
            deletarConta(conta)
        elif opcao == 4:
            conta = int(input('Digite o número da conta: '))
            consultarCliente(conta)
        elif opcao == 5:
            listarTodasContas()
        elif opcao == 6:
            conta = int(input('Digite o número da conta: '))
            consulta.consultarsaldo(conta)
        elif opcao == 7:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor do depósito: '))
            deposito.depositar(conta, valor)
        elif opcao == 8:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor do saque: '))
            saque.sacar(conta, valor)
        elif opcao == 9:
            contaOrigem = int(input('Digite o número da conta: '))
            contaDestino = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor de transferencia: '))
            transferencia.transferir(contaOrigem, contaDestino, valor)
        elif opcao == 10:
            print('---- VOCÊ SAIU DO PROGRAMA ----')
            break
        menu()
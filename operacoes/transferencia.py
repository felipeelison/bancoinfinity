from banco import obterConta, banco

def trasnferir(contaOri: int, contaDes: int, valor: float) -> None:
    contaOrigem = obterConta(contaOri)
    contaDestino = obterConta(contaDes)

    if contaOrigem and contaDestino:
        if contaOrigem['saldo'] >= valor:
            contaOrigem['saldo'] -= valor
            contaDestino['saldo'] += valor
            print('transferência realizada com sucesso!')
        else:
            print('saldo insuficiente!')
    else:
        print('Uma ou mais contas não existem!')

if __name__ == "__main__":
    trasnferir(1, 2, 159.99)
    print(banco)
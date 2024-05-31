saldo = 0

contagem_saques = 3 #usuario só tem 3 saques diarios com limite de R$500,00

extrato_transacoes = []


def extrato():
    global saldo
    texto_extrato = []
    for transacao in extrato_transacoes:
        texto_extrato.append(transacao)
    texto_extrato.append(f'Seu saldo atual é de R${saldo:.2f}')
    print("\n".join(texto_extrato))



def depositar(valor_deposito):
    if valor_deposito > 0:
        global saldo 
        global extrato
        saldo = saldo + valor_deposito
        
        print(f'Você depositou R${valor_deposito:.2f}')

        extrato_transacoes.append(f'Depósito no valor de R${valor_deposito:.2f}')
        

    elif valor_deposito == 0:
        print('Insira um valor maior que 0')

    else:
        print('Você não pode depositar um numero negativo')




def sacar(valor_saque):
    global contagem_saques 
    global saldo

    if valor_saque > 0 and valor_saque <= saldo and valor_saque <= 500 and contagem_saques > 0:
        saldo = saldo - valor_saque
        print(f'Você sacou R${valor_saque:.2f}')
        contagem_saques = contagem_saques - 1

        extrato_transacoes.append(f'Saque no valor de R${valor_saque:.2f}')


    elif valor_saque > saldo:
        print('Você não possui saldo suficiente para realizar essa operação')

    elif contagem_saques == 0:
        print('Você atingiu o seu numero maximo de saques diarios')

    elif valor_saque == 0:
        print('Insira um valor maior que 0 para realizar o saque')

    elif valor_saque < 0:
        print('Você não pode sacar um numero negativo')


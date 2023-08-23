print('Bem-vindo ao Pet-shop da Micaela Milman\n')

preco = 0
multip = 0
def pesoCachorro():  #função para pessoa inserir o peso do cachorro
    while True:
        try:
            peso = int(input('Qual é o peso do seu cachorro (kg): ')) #input para pessoa digitar o peso do cachorro
            if peso < 3:
                preco = 40
                return preco
            elif peso >= 3 and peso < 10:
                preco = 50
                return preco
            elif peso >= 10 and peso < 30:
                preco = 60
                return preco
            if peso >= 30 and peso < 50:
                preco = 70
                return preco
            else:
                print('Não aceitamos cachorros com esse peso. Tente novamente') #erro de peso
        except ValueError:
            print('Você digitou um valor não numérico.\nPor favor, digite o peso do cachorro novamente.') #erro de valor ñ numérico
def peloCachorro():  # Função para pessoa escolher o pelo do cachorro
    while True:
        pelo_cachorro = input('''Qual é o tipo de pelo do seu cachorro \n
        C - Pelo Curto\n
        M = Pelo Médio\n
        L = Pelo Longo\n
        >> ''') #menú
        pelo_cachorro = pelo_cachorro.upper()
        if pelo_cachorro == 'C':
            multip = 1
            return multip
        elif pelo_cachorro == 'M':
            multip = 1.5
            return multip
        elif pelo_cachorro == 'L':
            multip = 2
            return multip
        else:
            print('Você inseriu uma opção inválida. Digite uma das opções acima.') #erro se a pessoa não escolher entre C,M e L
def servicoExtra():  # Função para pessoa escolher um extra
    acumulador = 0
    while True:
        extra = input('''Deseja adicionar algum serviço adicional?: \n  
        0 - Não, desejo finalizar.\n
        1 - Cortes de unhas - R$10,00\n
        2 - Escovação de dentes - R$12,00\n
        3 - Limpeza de orelhas - R$15,00\n
        >>  ''') #menú 2
        if extra == '0':
            return acumulador
        elif extra == '1':
            acumulador += 10
            continue
        elif extra == '2':
            acumulador += 12
            continue
        elif extra == '3':
            acumulador += 15
            continue
        else:
            print('Você inseriu uma opção inválida. Digite uma das opções acima.')


# variáveis
peso_cachorro = pesoCachorro()
print('-' * 40)
pelo_cachorro = peloCachorro()
print('-' * 40)
servico_extra = servicoExtra()
print('-' * 40)

total = (peso_cachorro * pelo_cachorro) + servico_extra  # total pelo valor dos serviços
print(f'Seu total a pagar é: R${total:.2f}\nO peso do cachorro é: R${peso_cachorro:.2f} * O pelo do cachorro é: R${pelo_cachorro:.2f} + serviço(s) adicionais escolhidos: R${servico_extra:.2f})')
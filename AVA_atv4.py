print('Controle de Colaboradores da Micaela Milman')

lista_colaboradores = []
id_colaborador = 0


def cadastrar_colaboradores(id):  #função de cadastro do colaborador
    print('\n---------- MENU DE CADASTRO ----------\n')
    print('Cadastre o Colaborador: ')
    nome = input('Qual o nome do colaborador: ')
    setor = input('Qual o setor de trabalho do colaborador: ')
    salario = float(input('Quanto será o salário do colaborador: R$ '))

    dicionario_colaborador = {
        'id': id_colaborador,
        'nome': nome,
        'setor': setor,
        'salario': salario,
    }
    lista_colaboradores.append(dicionario_colaborador.copy())
def consultar_colaboradores():  #consulta de colaborador
    print('\n---------- MENU DE CONSULTA ----------\n')
    print('Consultar Colaborador: ')
    while True:  # loop de menu para consulta colaborador(a)
        consult_colab = input('''Digite a opcão desejada:
                                       1 - Consultar todos os colaboradores
                                       2 - Consultar por Id
                                       3 - Consultar por setor
                                       4 - Retornar ao menu principal
                                       >>> ''') #menu
        if consult_colab == '1':  #se consultar todos
            for colaborador in lista_colaboradores:
                print('-' * 30)
                for key, value in colaborador.items():
                    print(f'{key} : {value}')
                print('-' * 30)
        elif consult_colab == '2':  #se consultar por id
            id = int(input('Digite o ID do colaborador: '))
            for colaborador in lista_colaboradores:
                if colaborador['id'] == id:
                    print('-' * 30)
                    for key, value in colaborador.items():
                        print(f'{key} : {value}')
                    print('-' * 30)
        elif consult_colab == '3':  #se consultar por setor
            setor_colab = input('Digite o Setor do colaborador: ')
            for setor in lista_colaboradores:
                if setor['setor'] == setor_colab:
                    print('-' * 30)
                    for key, value in setor.items():
                        print(f'{key} : {value}')
                    print('-' * 30)
        elif consult_colab == '4':  #voltar pro menu
            return
        else:  #erro que volta pro inicio do laço
            print('Opção inválida. Tente novamente')
            continue
def remover_colaboradores():  #função remover colaborador
    id = int(input('Digite o ID do colaborador que será removido: '))
    for colaborador in lista_colaboradores:
        if colaborador['id'] == id:
            lista_colaboradores.remove(colaborador)
            print('\nColaborador REMOVIDO com sucesso!\n')

#programa principal:

while True:  #menu principal
    print('\n---------- MENU PRINCIPAL ----------\n')
    print('Cadastro, consulta ou remoção de colaborador')
    menu = input('''Digite a opcão desejada:
                 1 - Cadastrar colaborador
                 2 - Consultar Colaborador
                 3 - Remover colaborador
                 4 - Encerrar programa
                 >>> ''') #menu

    if menu == '1':  # Cadastro
        id_colaborador =  id_colaborador +1
        cadastrar_colaboradores(id_colaborador)
    elif menu == '2':  #consulta
        consultar_colaboradores()
    elif menu == '3':
        remover_colaboradores()
    elif menu == '4':
        print('Programa finalizado')
        break
    else:
        print('Opção inválida. Tente novamente')
        continue

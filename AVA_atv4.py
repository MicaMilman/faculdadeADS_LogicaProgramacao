print('\n Controle de Colaboradores da Micaela Milman')

lista_colaboradores = []
id_colaborador = 0


def cadastrar_colaboradores(id):  #função de cadastro do colaborador
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
    print('Consultar Colaborador: ')
    while True:  # loop de menu para consulta colaborador(a)
        consult_colab = input('''Digite a opcão desejada: \n 
                                       1 - Consultar todos os colaboradores\n
                                       2 - Consultar por Id\n
                                       3 - Consultar por setor\n
                                       4 - Retornar ao menu principal\n
                                       >>> ''') #menu
        if consult_colab == '1':  #se consultar todos
            print('Você escolheu consultar todos os colaboradores: ')
            for colaborador in lista_colaboradores:
                print('-' * 30)
                for key, value in colaborador.items():
                    print(f'{key} : {value}')
                print('-' * 30)
        elif consult_colab == '2':  #se consultar por id
            print('Você escolheu consultar por Id: ')
            id = int(input('Digite o ID do colaborador: '))
            for colaborador in lista_colaboradores:
                if colaborador['id'] == id:
                    print('-' * 30)
                    for key, value in colaborador.items():
                        print(f'{key} : {value}')
                    print('-' * 30)
        elif consult_colab == '3':  #se consultar por setor
            print('Você escolheu consultar por Setor: ')
            setor_colab = input('Digite o Setor do colaborador: ')
            for setor in lista_colaboradores:
                if setor['setor'] == setor_colab:
                    print('-' * 30)
                    for key, value in setor.items():
                        print(f'{key} : {value}')
                    print('-' * 30)
        elif consult_colab == '4':  #voltar pro menú
            return
        else:  #erro que volta pro inicio do laço
            print('Opção inválida. Tente novamente')
            continue
def remover_colaboradores():  #função remover colaborador
    print('Você escolheu remover colaborador: ')
    id = int(input('Entre com o ID do colaborador que deseja remover: '))
    for colaborador in lista_colaboradores:
        if colaborador['id'] == id:
            lista_colaboradores.remove(colaborador)
            print('Colaborador REMOVIDO com sucesso!')

#programa principal:

while True:  #menu principal
    print('Cadastro, consulta ou remoção de colaborador')
    menu = input('''Digite a opcão desejada: \n
                 1 - Cadastrar colaborador\n
                 2 - Consultar Colaborador\n
                 3 - Remover colaborador\n
                 4 - Encerrar programa\n
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

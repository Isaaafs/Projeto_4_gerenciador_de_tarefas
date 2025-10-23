import os

tarefas = {
    "tarefas" : ["arrumar o quarto","lavar a louça"],
    "datas" : ["17/10","17/10"]
}

def mostrar_tarefas():
    barra = f'|{30*'-'}|'
    print(barra)
    for i in range(len(tarefas['tarefas'])):
        print(f'| {i+1} - Tarefa: {tarefas['tarefas'][i]} | Datas: {tarefas['datas'][i]}')
    input('| Aperte "ENTER" para continuar...')


def adiconar_tarefas():
    barra = f'|{30*'-'}|'
    print(barra)
    tarefa = input('| Nome da tarefa: ')
    data = input('| Data:')
    tarefas['tarefas'].append(tarefa)
    tarefas['datas'].append(data)
    print('| Tarefa concluida com sucesso')
    input('| Aperte "ENTER" para continuar...')

def remover_tarefas():
    barra = f'|{30*'-'}|'
    print(barra)

    for i in range(len(tarefas['tarefas'])):
        print(f'| {i+1} - Tarefa: {tarefas['tarefas'][i]} | Datas: {tarefas['datas'][i]}')
    id_tarefa = int(input('Digite o numero da tarefa que deseja remover: '))

    if id_tarefa > 0:
        tarefas = tarefas['tarefas'].pop(id_tarefa-1)
        tarefas['datas'].pop(id_tarefa-1)
    else:
        print('| ID invalido')

    print('| tarefa {tarefas} removida com sucesso!')
    input('| Aperte "ENTER" para continuar...')

def menu():
    while True:
        try:
            os.system('cls')
            barra = f'|{30*'-'}|'
            print(barra)
            print('| Gerenciador de tarefas ')
            print(barra)
            print('| 1 - Mostra tarefas')
            print('| 2 - adiconar tarefas')
            print('| 3 - Remover tarefas')
            print('| 4 - Sair')
            print(barra)
            opc = int(input('| Escolha o numero da opção: '))
            if opc == 1:
                os.system('cls')
                mostrar_tarefas()
            elif opc == 2:
                os.system('cls')
                adiconar_tarefas()
            elif opc == 3:
                os.system('cls')
                remover_tarefas()
            elif opc == 4:
                print('Saindo do programa...')
                break
            else:
                os.system('cls')
                print('| Opção invalida!')
                input('| Aperte "ENTER" para continuar...')
        except:
            print('| Erro! escolha uma opção valida')
            input('| Aperte "ENTER" para continuar...')

menu()
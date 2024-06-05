import json

# Lista de tarefas (simulando o banco de dados)
tarefas = []

def adicionar_tarefa(descricao):
    tarefas.append({'descricao': descricao, 'concluida': False})

def listar_tarefas():
    for tarefa in tarefas:
        status = "Concluída" if tarefa['concluida'] else "Pendente"
        print(f"{tarefa['descricao']} ({status})")

def main():
    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Descrição da tarefa: ")
            adicionar_tarefa(descricao)
            print("Tarefa adicionada com sucesso!")
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

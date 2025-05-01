# Criar lista para armazenar as tarefas
tarefas = []

def adicionar_tarefa():
    nome = input('Nome da tarefa: ')
    descricao = input('Descrição da tarefa: ')
    prioridade = input('Prioridade da tarefa (Alta, Média, Baixa): ')
    categoria = input('Categoria da tarefa: ')
    tarefa ={
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluida': False,
    }
    # Adicionar tarefas a lista
    tarefas.append(tarefa)
    print('Tarefa adicionada com sucesso!')

# Listar tarefas
def listar():
     if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.") 
     else:
          for i, tarefa in enumerate(tarefas): 
            print(f"{i}. {tarefa['nome']} - {'Concluída' if tarefa['concluida'] else 'Pendente'}")
            print(f"   Descrição: {tarefa['descricao']}")
            print(f"   Prioridade: {tarefa['prioridade']}")
            print(f"   Categoria: {tarefa['categoria']}")

# Marcar tarefas como concluida
def marcar_tarefas_concluidas():
    listar()  
    indice = int(input("Digite o número da tarefa concluída: "))
    if 0 <= indice < len(tarefas): 
        tarefas[indice]['concluida'] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Índice inválido.")

# Exibir tarefa por prioridade ou categoria

def exibir_por_prioridade():
    prioridade = input("Digite a prioridade que deseja ver (Alta, Média, Baixa): ")
    for tarefa in tarefas:
        if tarefa['prioridade'].lower() == prioridade.lower(): 
            print(f"- {tarefa['nome']} ({'Concluída' if tarefa['concluida'] else 'Pendente'})")

def exibir_por_categoria():
    categoria = input("Digite a categoria que deseja ver: ")
    for tarefa in tarefas:
        if tarefa['categoria'].lower() == categoria.lower():
            print(f"- {tarefa['nome']} ({'Concluída' if tarefa['concluida'] else 'Pendente'})")

# Menu
def menu():
    print('Menu: ')
    print('0) Sair')
    print('1) Adicionar tarefa')
    print('2) Listar tarefas')
    print('3) Marcar como concluida')
    print('4) Exibir tarefa por prioridade')
    print('5) Exibir tarefa por categoria')

while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "0":
        print("Saindo do programa!")
        break
    elif opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        marcar_tarefas_concluidas()
    elif opcao == "4":
        exibir_por_prioridade()
    elif opcao == "5":
        exibir_por_categoria()
    else:
        print("Opção inválida, tente novamente.")
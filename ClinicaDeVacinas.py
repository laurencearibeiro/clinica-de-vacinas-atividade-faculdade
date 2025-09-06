# Sistema de Atendimento de uma Clínica de Vacinas

pacientes = [] # Lista de pacientes cadastrados
fila_vacinacao = [] # Fila de espera para vacinação
historico_vacinados = [] # Pilha de pacientes vacinados

# Construindo a função do menu principal

def menu():
    print("\n==== Clínica de Vacinas ====")
    print("1 - Cadastrar paciente")
    print("2 - Adicionar paciente na fila de vacinação")
    print("3 - Chamar próximo paciente para vacinação")
    print("4 - Ver fila de espera")
    print("5 - Ver histórico de pacientes vacinados")
    print("6 - Buscar paciente cadastrado")
    print("7 - Listar pacientes cadastrados ordenados")
    print("8 - Sair")

def cadastrar_pacientes(): # 1
    nome = input("Digite o nome do paciente: ")
    codigo = input("Digite o código do paciente: ")

    # obrigatório inserir os dados
    if not nome or not codigo:
        print("Erro! Nome e código não podem ser vazios.")
        return

    if codigo.isdigit(): # retorna True se a condição for dígitos
        codigo = int(codigo)
        paciente = [nome, codigo]
        pacientes.append(paciente)
        print(f"Paciente cadastrado com sucesso! Nome: {nome.upper()} | Código: {codigo}")
    else:
        print("Erro ao cadastrar o paciente. Tente novamente.")

def buscar_paciente(codigo): 
    for paciente in pacientes:
        if paciente[1] == codigo:
            return paciente
    return None

def adicionar_na_fila(): # 2
    codigo = int(input("Digite o código do paciente para adicionar na fila: "))
    paciente = buscar_paciente(codigo)
    if paciente:
        fila_vacinacao.append(paciente)
        print("Paciente adicionado na fila de vacinação.")
    else:
        print("Paciente não encontrado no cadastro.")

def chamar_proximo(): # 3
    if len(fila_vacinacao) > 0:
        paciente = fila_vacinacao.pop(0)
        historico_vacinados.append(paciente)
        print(f"Chamando paciente para vacinação: {paciente[0]}")
    else:
        print("Fila de vacinação vazia.")

def ver_fila(): # 4
    if fila_vacinacao == 0:
        print("Fila de vacinação vazia.")
    else:
        print("Fila de vacinação: ")
        for paciente in fila_vacinacao:
            print(f"- {paciente[0]} (Código: {paciente[1]})")

def ver_historico(): # 5
    if len(historico_vacinados) == 0:
        print("Histórico vazio.")
    else:
        print("Histórico de pacientes vacinados:")
        for paciente in reversed(historico_vacinados):
            print(f"- {paciente[0]} (Código: {paciente[1]})")

def buscar_paciente_cadastro(): # 6
    codigo = int(input("Digite o código do paciente que deseja buscar: "))
    paciente = buscar_paciente(codigo)
    if paciente: # se o paciente existe
        print(f"Nome do paciente: {paciente[0]}")
    else: 
        print("O paciente não foi encontrado no cadastro de pacientes da clínica.")

def listar_pacientes_ordenados(): # 7
    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return 
    
    criterio = input("Ordenar por (1) Nome ou (2) Código? ")
    lista_ordenada = pacientes.copy()

# ordenação usando Selection Sort
    for i in range(len(lista_ordenada)): # posicao atual que vamos preencher (i)
        min_idx = i
        for j in range(i + 1, len(lista_ordenada)):
            if criterio == "1":
                if lista_ordenada[j][0].lower() < lista_ordenada[min_idx][0]:
                    min_idx = j
            elif criterio == "2":
                if lista_ordenada[j][1] < lista_ordenada[min_idx][1]:
                    min_idx = j
        lista_ordenada[i], lista_ordenada[min_idx] = lista_ordenada[min_idx], lista_ordenada[i]
    
    print("\n Pacientes cadastrados ordenados: ")
    for paciente in lista_ordenada:
        print(f"- {paciente[0]} (Código: {paciente[1]})")

# ---> Início do Programa <---

if __name__ == "__main__":
    while True:
        menu()
        opcao = int(input("Escolhe uma opção: "))
    
        match opcao:
            case 1:
                cadastrar_pacientes()
            case 2:
                adicionar_na_fila()
            case 3:
                chamar_proximo()
            case 4:
                ver_fila()
            case 5:
                ver_historico()
            case 6:
                buscar_paciente_cadastro()
            case 7:
                listar_pacientes_ordenados()
            case 8:
                print("Saindo... Obrigado por usar o nosso sistema!")
                break
            case _:
                print("Opção inválida, tente novamente.")
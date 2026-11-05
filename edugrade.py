# edugrade.py - Sistema de Gestão Escolar (CLI)

# Base de dados em memória (Lista de Dicionários)
alunos = []

def ler_float(mensagem, min_val, max_val):
    """Lê um valor numérico decimal com tratamento de erros e limites."""
    while True:
        try:
            valor = float(input(mensagem))
            if min_val <= valor <= max_val:
                return valor
            print(f"Erro: O valor deve estar entre {min_val} e {max_val}.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número.")

def ler_nome(mensagem):
    """Lê um nome válido garantindo que não seja apenas números ou vazio."""
    while True:
        nome = input(mensagem).strip()
        if not nome:
            print("Erro: O nome não pode ser vazio.")
        elif nome.isdigit():
            print("Erro: O nome do aluno não pode conter apenas números.")
        else:
            return nome

def calcular_situacao(media, presenca):
    """Aplica as Regras de Negócio (RN01 e RN02) para definir a situação do aluno."""
    if presenca < 75.0:
        return "Reprovado por Faltas"
    elif media >= 7.0:
        return "Aprovado"
    elif 5.0 <= media < 7.0:
        return "Recuperação"
    else:
        return "Reprovado por Nota"

def cadastrar_aluno():
    print("\n--- CADASTRO DE ALUNO E NOTAS ---")
    nome = ler_nome("Nome do aluno: ")
    
    disciplina = input("Disciplina: ").strip()
    while not disciplina:
        print("Erro: A disciplina não pode ser vazia.")
        disciplina = input("Disciplina: ").strip()

    presenca = ler_float("Porcentagem de presença (0 a 100%): ", 0.0, 100.0)
    
    nota1 = ler_float("Nota 1 (0 a 10): ", 0.0, 10.0)
    nota2 = ler_float("Nota 2 (0 a 10): ", 0.0, 10.0)
    nota3 = ler_float("Nota 3 (0 a 10): ", 0.0, 10.0)
    
    media = (nota1 + nota2 + nota3) / 3.0
    status = calcular_situacao(media, presenca)
    
    aluno = {
        "nome": nome,
        "disciplina": disciplina,
        "presenca": presenca,
        "notas": [nota1, nota2, nota3],
        "media": media,
        "status": status
    }
    
    alunos.append(aluno)
    print(f"\n[✓] Aluno(a) '{nome}' cadastrado(a) com sucesso!")
    input("\nPressione ENTER para voltar ao menu principal...")

def listar_alunos():
    print("\n--- LISTA DE ALUNOS ---")
    if not alunos:
        print("Nenhum aluno cadastrado até o momento.")
    else:
        print(f"{'Nome':<20} | {'Disciplina':<15} | {'Média':<6} | {'Presença':<8} | {'Status'}")
        print("-" * 70)
        for a in alunos:
            print(f"{a['nome']:<20} | {a['disciplina']:<15} | {a['media']:<6.1f} | {a['presenca']:<7.1f}% | {a['status']}")
    
    input("\nPressione ENTER para voltar ao menu principal...")

def buscar_boletim():
    print("\n--- CONSULTA DE BOLETIM ---")
    if not alunos:
        print("Nenhum aluno cadastrado no sistema.")
    else:
        termo = input("Digite o nome do aluno para buscar: ").strip().lower()
        while not termo:
            print("Erro: Digite um nome para buscar.")
            termo = input("Digite o nome do aluno para buscar: ").strip().lower()

        encontrados = [a for a in alunos if termo in a['nome'].lower()]
        
        if not encontrados:
            print("Aluno não encontrado.")
        else:
            for a in encontrados:
                print("\n========================================")
                print(f" BOLETIM ESCOLAR: {a['nome'].upper()}")
                print("========================================")
                print(f"Disciplina : {a['disciplina']}")
                print(f"Presença   : {a['presenca']:.1f}%")
                print(f"Notas      : N1 = {a['notas'][0]:.1f} | N2 = {a['notas'][1]:.1f} | N3 = {a['notas'][2]:.1f}")
                print(f"Média Final: {a['media']:.2f}")
                print(f"Situação   : {a['status']}")
                print("========================================")
    
    input("\nPressione ENTER para voltar ao menu principal...")

def menu_principal():
    while True:
        print("\n========================================")
        print("           SISTEMA EDUGRADE             ")
        print("========================================")
        print("1. Cadastrar Aluno e Lançar Notas")
        print("2. Listar Todos os Alunos")
        print("3. Buscar Boletim por Nome")
        print("4. Sair")
        print("----------------------------------------")
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            buscar_boletim()
        elif opcao == '4':
            print("\nEncerrando o EduGrade. Até logo!")
            break
        else:
            print("Opção inválida! Escolha um número entre 1 e 4.")

if __name__ == "__main__":
    menu_principal()
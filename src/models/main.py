from src.models.sistema import Sistema
from src.models.aluno import Aluno

def menu():
    sistema = Sistema()

    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar Aluno")
        print("2. Calcular Média de um Aluno")
        print("3. Listar Alunos")
        print("4. Calcular Média da Turma")
        print("5. Exibir Relatório")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do aluno: ")
            matricula = input("Matrícula: ")
            notas = list(map(float, input("Notas (separadas por espaço): ").split()))
            aluno = Aluno(nome, matricula, notas)
            sistema.cadastrar_aluno(aluno)
            print(f"Aluno {nome} cadastrado com sucesso.")

        elif opcao == '2':
            matricula = input("Informe a matrícula do aluno: ")
            aluno = sistema.turma.buscar_aluno(matricula)
            if aluno:
                print(f"A média de {aluno.nome} é: {aluno.calcular_media()}")
            else:
                print("Aluno não encontrado.")

        elif opcao == '3':
            alunos = sistema.listar_alunos()
            if alunos:
                for aluno in alunos:
                    print(f"Nome: {aluno.nome}, Matrícula: {aluno.matricula}")
            else:
                print("Não há alunos cadastrados.")

        elif opcao == '4':
            media = sistema.calcular_media_turma()
            print(f"A média geral da turma é: {media}")

        elif opcao == '5':
            sistema.exibir_relatorio()

        elif opcao == '6':
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()

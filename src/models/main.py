class Aluno:
    def __init__(self, nome: str, matricula: str, notas: list = None):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas if notas else []

    def adicionar_nota(self, nota: float):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            raise ValueError("A nota deve estar entre 0 e 10.")

    def calcular_media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0.0

class Turma:
    def __init__(self, nome: str, codigo: str):
        self.nome = nome
        self.codigo = codigo
        self.alunos = []

    def adicionar_aluno(self, aluno: Aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
        else:
            raise ValueError(f"O aluno {aluno.nome} já está na turma.")

    def listar_alunos(self):
        if not self.alunos:
            return "Não há alunos na turma."
        else:
            resultado = f'Alunos na turma {self.nome}:'
            for aluno in self.alunos:
                resultado += f"\nNome: {aluno.nome}, Matrícula: {aluno.matricula}"
            return resultado 

    def calcular_media_turma(self):
        if not self.alunos:
            return 0.0 
        return sum(aluno.calcular_media() for aluno in self.alunos) / len(self.alunos)

    def buscar_aluno_por_matricula(self, matricula: str):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

class Sistema:
    def __init__(self):
        self.turma = Turma(nome="Turma A", codigo="001")

    def cadastrar_aluno(self, aluno):
        self.turma.adicionar_aluno(aluno)

    def listar_alunos(self):
        return self.turma.listar_alunos()

    def calcular_media_turma(self):
        return self.turma.calcular_media_turma()
    
    def exibir_relatorio(self):
        if not self.turma.alunos:
            print("Não há alunos cadastrados.")
            return
    
        for aluno in self.turma.alunos:
            print(f"{aluno.nome} - Média: {aluno.calcular_media()}")

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
            aluno = sistema.turma.buscar_aluno_por_matricula(matricula)
            if aluno:
                print(f"A média de {aluno.nome} é: {aluno.calcular_media()}")
            else:
                print("Aluno não encontrado.")

        elif opcao == '3':
            if sistema.turma.alunos:
                for aluno in sistema.turma.alunos:
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
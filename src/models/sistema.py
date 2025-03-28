from src.models.turma import Turma

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
        alunos = self.listar_alunos()
        for aluno in alunos:
            print(f"{aluno.nome} - Média: {aluno.calcular_media()}")

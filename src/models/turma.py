from aluno import Aluno

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
            print("Não há alunos na turma.")
        else:
            print(f"Alunos na turma {self.nome}:")
            resultado = f'Alunos na turma {self.nome}:'
            for aluno in self.alunos:
                resultado += f"\nNome: {aluno.nome}, Matrícula: {aluno.matricula}"
            return resultado

    def calcular_media_turma(self):
        if not self.alunos:
            return 0.0
        soma_medias = sum(aluno.calcular_media() for aluno in self.alunos)
        return soma_medias / len(self.alunos)

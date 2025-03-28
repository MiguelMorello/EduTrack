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

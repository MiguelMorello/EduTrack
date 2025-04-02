import unittest
from src.models.main import Aluno, Turma

class TestTurma(unittest.TestCase):
    def setUp(self):
        self.aluno1 = Aluno("João Silva", "12345")
        self.aluno2 = Aluno("Maria Oliveira", "67890")
        self.turma = Turma("Turma A", "TURMA01")

    def test_adicionar_aluno(self):
        self.turma.adicionar_aluno(self.aluno1)
        self.assertIn(self.aluno1, self.turma.alunos)

    def test_adicionar_aluno_duplicado(self):
        self.turma.adicionar_aluno(self.aluno1)
        with self.assertRaises(ValueError):
            self.turma.adicionar_aluno(self.aluno1)

    def test_listar_alunos(self):
        self.turma.adicionar_aluno(self.aluno1)
        self.turma.adicionar_aluno(self.aluno2)
        resultado = self.turma.listar_alunos()
        self.assertIn("Nome: João Silva, Matrícula: 12345", resultado)
        self.assertIn("Nome: Maria Oliveira, Matrícula: 67890", resultado)


    def test_calcular_media_turma(self):
        self.aluno1.adicionar_nota(8)
        self.aluno1.adicionar_nota(9)
        self.aluno2.adicionar_nota(7)
        self.aluno2.adicionar_nota(6)
        self.turma.adicionar_aluno(self.aluno1)
        self.turma.adicionar_aluno(self.aluno2)
        self.assertEqual(self.turma.calcular_media_turma(), 7.5,)

if __name__ == "__main__":
    unittest.main()

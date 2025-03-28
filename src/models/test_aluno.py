import unittest
from src.models.aluno import Aluno

class TestAluno(unittest.TestCase):
    def setUp(self):
        self.aluno = Aluno("João Silva", "12345")

    def test_criacao_aluno(self):
        self.assertEqual(self.aluno.nome, "João Silva")
        self.assertEqual(self.aluno.matricula, "12345")
        self.assertEqual(self.aluno.notas, [])

    def test_adicionar_nota_valida(self):

        self.aluno.adicionar_nota(8.5)
        self.assertIn(8.5, self.aluno.notas)

    def test_adicionar_nota_invalida(self):

        with self.assertRaises(ValueError):
            self.aluno.adicionar_nota(15)

    def test_calcular_media(self):
        self.aluno.adicionar_nota(7)
        self.aluno.adicionar_nota(9)
        self.assertEqual(self.aluno.calcular_media(), 8.0)

if __name__ == "__main__":
    unittest.main()

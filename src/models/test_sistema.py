import unittest
from models.sistema import Sistema
from models.aluno import Aluno
from models.turma import Turma

class TestSistema(unittest.TestCase):

    def setUp(self):
        self.sistema = Sistema()
        self.turma = Turma(nome="Turma A", codigo='100')
        self.sistema.turma = self.turma
        self.aluno1 = Aluno("João Silva", "12345", [7.0, 8.0, 6.5])
        self.aluno2 = Aluno("Maria Oliveira", "67890", [9.0, 7.5, 8.0])
        self.sistema.cadastrar_aluno(self.aluno1)
        self.sistema.cadastrar_aluno(self.aluno2)

    def test_cadastrar_aluno(self):
        aluno3 = Aluno("Lucas Pereira", "11223", [10.0, 9.5, 8.5])
        self.sistema.cadastrar_aluno(aluno3)
        alunos = self.sistema.listar_alunos()
        self.assertIn(aluno3.nome, alunos)


    def test_calcular_media_aluno(self):
        media_aluno1 = self.aluno1.calcular_media()
        self.assertEqual(media_aluno1, 7.166666666666667)  

    def test_listar_alunos(self):
        alunos = self.sistema.listar_alunos()
        self.assertEqual(len(alunos), 2)
        self.assertEqual(alunos[0].nome, "João Silva")
        self.assertEqual(alunos[1].nome, "Maria Oliveira")

    def test_calcular_media_turma(self):
        media_turma = self.sistema.calcular_media_turma()
        self.assertEqual(media_turma, 7.666666666666666) 

    def test_exibir_relatorio(self):
        with self.assertLogs() as log:
            self.sistema.exibir_relatorio()
            self.assertIn("João Silva", log.output[0])
            self.assertIn("Maria Oliveira", log.output[0])


if __name__ == "__main__":
    unittest.main()

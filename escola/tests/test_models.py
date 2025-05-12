from django.test import TestCase
from escola.models import Estudante,Curso,Matricula

class ModelEstudanteTestCase(TestCase):
    # def teste_falha(self):
    #     self.fail("Teste falhou! :: (")
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'Testerson@gmail.com',
            cpf = '37926838063',
            data_nascimento = '2023-02-02',
            celular = '86 99999-9999'
        )
    
    def test_verifica_atributos_de_estudante(self):
        """Teste que verifica os atributos do modelo de Estudante."""
        self.assertEqual(self.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.estudante.email, 'Testerson@gmail.com')
        self.assertEqual(self.estudante.cpf, '37926838063')
        self.assertEqual(self.estudante.data_nascimento, '2023-02-02')
        self.assertEqual(self.estudante.celular, '86 99999-9999')

class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'TST123',
            descricao = 'Teste de Modelo',
            nivel = 'B'
        )

    def test_verifica_atributos_de_curso(self):
        """Teste que verifica os atributos do modelo de Estudante."""
        self.assertEqual(self.curso.codigo, 'TST123')
        self.assertEqual(self.curso.descricao, 'Teste de Modelo')
        self.assertEqual(self.curso.nivel, 'B')

class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'Testerson@gmail.com',
            cpf = '37926838063',
            data_nascimento = '2023-02-02',
            celular = '86 99999-9999'
        )
        self.curso = Curso.objects.create(
            codigo = 'TST123',
            descricao = 'Teste de Modelo',
            nivel = 'B'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo= 'M'
        )
    
    def test_verifica_atributos_de_matricula(self):
        """Teste que verifica os atributos do modelo de Estudante."""
        self.assertEqual(self.matricula.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.matricula.curso.codigo, 'TST123')
        self.assertEqual(self.matricula.periodo,'M')
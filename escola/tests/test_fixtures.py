from django.test import TestCase
from escola.models import Estudante, Curso

class FixturesTestCase(TestCase):
   fixtures = ['prototipo_banco.json']

   def test_carregamento_da_fixtures(self):
      """Teste que verifica o carregamento da fixtures."""
      estudante = Estudante.objects.get(cpf='58083269824')
      curso = Curso.objects.get(pk=1)
      self.assertEqual(estudante.celular, "76 99462-4414")
      self.assertEqual(curso.codigo, 'POO')
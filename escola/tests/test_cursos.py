from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso
from escola.serializers import CursoSerializer

class CursosTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(
            username='admin',
            password='admin123'
        )
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)
        self.curso_01 = Curso.objects.create(
            codigo = 'TST1',
            descricao = 'Teste Curso Um',
            nivel = 'B'
            )
        self.curso_02 = Curso.objects.create(
            codigo = 'TST2',
            descricao = 'Teste Curso Dois',
            nivel = 'B'
        )

    def test_requisicao_get_para_listar_cursos(self):
        """Teste que verifica uma requisição GET para listar cursos."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_Um_curso(self):
        """Teste que verifica uma requisição GET para listar um curso."""
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso = Curso.objects.get(pk=1)
        dados_curso_serializados = CursoSerializer(instance=dados_curso).data
        self.assertEqual(response.data, dados_curso_serializados)

    def test_requisicao_post_para_criar_curso(self):
        """Teste que verifica uma requisição POST para criar um curso."""
        dados = {
            'codigo': 'TST3',
            'descricao': 'Teste Curso Três',
            'nivel': 'B'
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_um_curso(self):
        """Teste que verifica uma requisição DELETE para criar um curso."""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_um_curso(self):
        """Teste de requisição PUT para atualizar um curso."""
        dados = {
            'codigo': 'TSTX',
            'descricao': 'Teste Curso Extra',
            'nivel': 'B'
        }
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
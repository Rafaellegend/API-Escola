from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.usuario = User.objects.get(username='Rafael')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_01 = Estudante.objects.get(pk=1)
        self.estudante_02 = Estudante.objects.get(pk=2)

    def test_requisicao_get_para_listar_estudantes(self):
        """Teste que verifica uma requisição GET para listar estudantes."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_Um_estudante(self):
        """Teste que verifica uma requisição GET para listar um estudante."""
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance=dados_estudante).data
        self.assertEqual(response.data, dados_estudante_serializados)

    def test_requisicao_post_para_criar_estudante(self):
        """Teste que verifica uma requisição POST para criar um estudante."""
        dados = {
            'nome': 'Teste',
            'email': 'teste@gmail.com',
            'cpf': '68531672015',
            'data_nascimento': '1969-02-27',
            'celular': '65 99145-0773'
        }
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_um_estudante(self):
        """Teste de requisição DELETE para deletar um estudante."""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_um_estudante(self):
        """Teste de requisição PUT para atualizar um estudante."""
        dados = {
            'nome': 'Teste',
            'email': 'testeput@gmail.com',
            'cpf': '24869327040',
            'data_nascimento': '1969-02-27',
            'celular': '65 99145-0737'
        }
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
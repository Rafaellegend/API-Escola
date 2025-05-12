from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(
            username='admin',
            password='admin123'
        )
    
    def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste que verifica se o usuário pode se autenticar com credenciais corretas."""
        usuario = authenticate(username='admin', password='admin123')
        self.assertTrue((usuario is not None) and (usuario.is_authenticated))

    def test_autenticacao_user_com_username_incorretas(self):
        """Teste que verifica a autenticação com username incorreto."""
        usuario = authenticate(username='admininastro', password='admin123')
        self.assertFalse((usuario is not None) and (usuario.is_authenticated))    

    def test_autenticacao_user_com_senha_incorretas(self):
        """Teste que verifica a autenticação com senha incorreta."""
        usuario = authenticate(username='admin', password='admin')
        self.assertFalse((usuario is not None) and (usuario.is_authenticated))
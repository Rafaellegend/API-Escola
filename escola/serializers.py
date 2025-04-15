from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import invalid_celular,invalid_cpf,invalid_nome

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf' , 'data_nascimento', 'celular']

    def validate(self, data):
        if invalid_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve conter um valor valido.'})
        if invalid_nome(data['nome']):
            raise serializers.ValidationError({'nome':'O nome deve conter apenas letras.'})
        if invalid_celular(data['celular']):
            raise serializers.ValidationError({'celular':'O celular deve seguir o modelo 86 99999-9999.(Respeitando traços e espaços)'})
        return data


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self,obj):
        return obj.get_periodo_display()
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']
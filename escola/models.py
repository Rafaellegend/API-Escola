from django.db import models

'''
Modelo Estudante
    - Id
    - Nome
    - E-mail
        - Não pode estar em branco
    - CPF
        - Máximo de 11 caracteres
    - Data de Nascimento
    - Número de Celular
        - Máximo de 14 caracteres
'''
class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
    
'''
Model Curso
    - Id
    - Código
        - Máximo de 10 caracteres
    - Descrição
        - Não pode estar em Branco
    - Nível (Básico, Intermediário e Avançado)
        - Não pode estar em Branco
        - Não pode ser Nulo
        - Por padrão deve ser Básico
'''
class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )

    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100, blank=False)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default= 'B')

    def __str__(self):
        return self.codigo

'''
Modelo Matricula
    - Id
    - Relacionar com o modelo Estudante
        - Se o Estudante for deletado, todas as matrículas daquele estudante devem ser deletadas
    - Relacionar com o modelo Curso
        - Se o Curso for deletado, todas as matriculas daquele curso devem ser deletadas
    - Período (Matutino, Vespertino, Noturno)
        - Não pode estar em Branco
        - Não pode ser Nulo
        - Por padrão deve ser Matutino
'''
class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default= 'M')

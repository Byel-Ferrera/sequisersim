from django.db import models

class Aluno(models.Model):
    zona_residencial_choices = [
        ('Urbana', 'Urbana'),
        ('Rural', 'Rural'),
    ]

    tipo_instituicao_choices = [
        ('Pública', 'Pública'),
        ('Privada', 'Privada'),
    ]
   
    nivel_de_ensino_choices = [
        ('Sem escolaridade', 'Sem escolaridade'),
        ('Fundamental Incompleto', 'Fundamental Incompleto'),
        ('Fundamental Completo', 'Fundamental Completo'),
        ('Médio Incompleto', 'Médio Incompleto'),
        ('Médio Completo', 'Médio Completo'),
        ('Superior Incompleto', 'Superior Incompleto'),
        ('Superior Completo', 'Superior Completo'),
    ]

    sexo_choices = [
        ('M', 'Masculino'), 
        ('F', 'Feminino'), 
        ('O', 'Outro'),
    ]

    etnia_choices = [
        ('Branca', 'Branca'),
        ('Preta', 'Preta'),
        ('Parda', 'Parda'),
        ('Amarela', 'Amarela'),
        ('Indígena', 'Indígena'),
        ('Não Declarada', 'Não Declarada'),
    ]

    nacionalidade_choices = [
        ('Brasileira', 'Brasileira'),
        ('Estrangeira', 'Estrangeira'),
    ]

    naturalidade_choices = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]

    estado_civil_choices = [
        ('Solteiro(a)', 'Solteiro(a)'),
        ('Casado(a)', 'Casado(a)'),
        ('Divorciado(a)', 'Divorciado(a)'),
        ('Viúvo(a)', 'Viúvo(a)'),
        ('Outro', 'Outro'),
    ]


    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=11, primary_key=True)
    data_de_nascimento = models.DateField()    
    sexo = models.CharField(max_length=1, choices=sexo_choices)
    etnia = models.CharField(max_length=50, choices=etnia_choices)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    foto_path = models.ImageField(upload_to='fotos_alunos/', blank=True, null=True)
    nacionalidade = models.CharField(max_length=50, choices=nacionalidade_choices)
    naturalidade = models.CharField(max_length=50, choices=naturalidade_choices)
    nome_social = models.CharField(max_length=100, blank=True, null=True)
    estado_civil = models.CharField(max_length=20, choices=estado_civil_choices)
    endereco = models.TextField()
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    zona_residencial = models.CharField(max_length=20, choices=zona_residencial_choices)
    possui_deficiencia = models.BooleanField()
    qual_deficiencia = models.CharField(max_length=100, blank=True, null=True)
    nivel_de_ensino = models.CharField(max_length=50, choices=nivel_de_ensino_choices)
    tipo_instituicao = models.CharField(max_length=50, choices=tipo_instituicao_choices)

    def __str__(self):
        return self.nome

#--------------------x-----------------------------------------x---------------------

class Curso(models.Model):
       
    tipo_curso_choices = [
        ('Presencial', 'Presencial'),
        ('EAD', 'EAD'),
        ('Híbrido', 'Híbrido'),
    ]

    nome = models.CharField(max_length=100, primary_key=True)
    descricao = models.TextField()
    tipo = models.CharField(max_length=50, choices=tipo_curso_choices)
    data_de_criação = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

#--------------------x-----------------------------------------x---------------------

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    descricao = models.TextField()
    carga_horaria = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

#--------------------x-----------------------------------------x---------------------

class Turma(models.Model):
       
    turno_choices = [
        ('Manhã', 'Manhã'),
        ('Tarde', 'Tarde'),
        ('Noite', 'Noite'),
    ]
       
    numero_da_turma = models.IntegerField(primary_key=True)
    turno = models.CharField(max_length=50, choices=turno_choices)
    inicio = models.DateField()
    fim = models.DateField()
    descricao = models.TextField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='turmas')

    def __str__(self):
        return f"{self.curso.nome} - {self.numero_da_turma} - {self.turno}"

#--------------------x-----------------------------------------x---------------------

class Atividades(models.Model):
    atividades = models.CharField(max_length=100, primary_key=True)
    descricao = models.TextField()

    def __str__(self):
        return self.atividades

#--------------------x-----------------------------------------x---------------------

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='matriculas')
    data_da_matricula = models.DateField(auto_now_add=True)
    data_do_desligamento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.aluno.nome} - {self.turma}"
    class Meta:
        unique_together = ('aluno', 'turma')

#--------------------x-----------------------------------------x---------------------

class Frequencia(models.Model):
    cpf_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='frequencias')
    numero_da_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='frequencias')
    nome_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='frequencias')
    id_atividade = models.IntegerField()
    data_da_atividade = models.DateField()
    presenca = models.BooleanField(help_text="Presente = Marcado | Ausente = Desmarcado")

    def __str__(self):
        return f"{self.cpf_aluno} - {self.nome_disciplina} - {self.numero_da_turma}"

        
#--------------------x-----------------------------------------x---------------------

class AvaliacaoAluno(models.Model):
    cpf_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='avaliacoes_aluno')
    numero_da_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='avaliacoes_aluno')
    nome_disciplina = models.CharField(max_length=100)
    id_atividade = models.ForeignKey(Atividades, on_delete=models.CASCADE, related_name='avaliacoes_aluno')
    data_da_atividade = models.DateField()
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.cpf_aluno} - {self.nota} - {self.id_atividade}"

#--------------------x-----------------------------------------x---------------------

class AvaliacaoCurso(models.Model):
    cpf_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='avaliacoes_curso')
    secao = models.CharField(max_length=50)
    pergunta = models.TextField()
    resposta = models.TextField()

    def __str__(self):
        return f"{self.cpf_aluno} - {self.secao}"

#--------------------x-----------------------------------------x---------------------

class Professor(models.Model):
    cpf = models.CharField(max_length=11, unique=True, primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    formacao = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

#--------------------x-----------------------------------------x---------------------

class Producao(models.Model):
      
    choise_situacao_pagamento = [
        ('Pendente', 'Pendente'),
        ('Pago', 'Pago'),
        ('Atrasado', 'Atrasado'),
    ]

    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='producoes')
    horas_trabalhadas = models.IntegerField()
    valor_hora = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()
    situação_pagamento = models.CharField(max_length=50, choices=choise_situacao_pagamento)
    competencia = models.CharField(max_length=7,help_text="Formato: MM/AAAA")
      
    def __str__(self):
        return self.professor.nome

#--------------------x-----------------------------------------x---------------------

class Professor_Turma_Disciplina(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='professor_turma_disciplina')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='professor_turma_disciplina')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='professor_turma_disciplina')

    def __str__(self):
        return f"{self.professor.cpf} - {self.turma.numero_da_turma} - {self.disciplina.nome}"



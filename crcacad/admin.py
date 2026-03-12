from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Professor)
admin.site.register(Producao)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(Atividades)
admin.site.register(Aluno)
admin.site.register(Frequencia)
admin.site.register(AvaliacaoAluno)
admin.site.register(AvaliacaoCurso)
admin.site.register(Professor_Turma_Disciplina)
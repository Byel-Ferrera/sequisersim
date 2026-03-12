from django import forms
from .models import *

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            'data_de_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        
class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'
        widgets = {
            'inicio': forms.DateInput(attrs={'type': 'date'}),
            'fim': forms.DateInput(attrs={'type': 'date'})
        }

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'

class AtividadesForm(forms.ModelForm):
    class Meta:
        model = Atividades
        fields = '__all__'

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'
        widgets = {
            'data_da_matricula': forms.DateInput(attrs={'type': 'date'}),
            'data_do_desligamento': forms.DateInput(attrs={'type': 'date'})
        }

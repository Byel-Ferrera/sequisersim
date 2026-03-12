from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import TemplateView


from crcacad.forms import *
from .models import *

class IndexView(TemplateView): template_name = 'crcacad/base.html'

def criar_alunos(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AlunoForm()
    return render(request, 'crcacad/forms/formsAluno.html', {'form': form})

def listar_alunos(request):
    alunos = Aluno.objects.prefetch_related('matriculas', 'frequencias', 'avaliacoes_aluno', 'avaliacoes_curso')
    return render(request, 'crcacad/listas/aluno.html', {'alunos': alunos})

def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    form = AlunoForm(request.POST or None,request.FILES or None, instance=aluno)
    if form.is_valid():
        form.save()
    return render(request, 'crcacad/forms/formsAluno.html', {'form': form})

def excluir_aluno(request, id):


    aluno = get_object_or_404(Aluno, pk=id)
    aluno.delete()
    return redirect('crcacad:lista_alunos')

def criar_cursos(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CursoForm()
    return render(request, 'crcacad/forms/formsCurso.html', {'form': form})

def listar_curso(request):
    cursos = Curso.objects.all()
    return render(request, 'crcacad/listas/curso.html', {'cursos': cursos})

def editar_curso(request, nome):
    curso = get_object_or_404(Curso, pk=nome)
    form = CursoForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save()
    return render(request, 'crcacad/forms/formsCurso.html', {'form': form})

def excluir_curso(request, nome):

    curso = get_object_or_404(Curso, pk=nome)
    curso.delete()
    return redirect('crcacad:listar_curso')

def criar_turma(request):
    form = TurmaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TurmaForm()
    return render(request, 'crcacad/forms/formsTurma.html', {'form': form})

def listar_turma(request):
    turmas = Turma.objects.select_related('curso').all()
    return render(request, 'crcacad/listas/turma.html', {'turmas': turmas})

def editar_turma(request, numero_da_turma):
    turma = get_object_or_404(Turma, pk=numero_da_turma)
    form = TurmaForm(request.POST or None, instance=turma)
    if form.is_valid():
        form.save()
    return render(request, 'crcacad/forms/formsTurma.html', {'form': form})

def excluir_turma(request, numero_da_turma):

    turma = get_object_or_404(Turma, pk=numero_da_turma)
    turma.delete()
    return redirect('crcacad:listar_turma')

def criar_professor(request):
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProfessorForm()
    return render(request, 'crcacad/forms/formsProfessor.html', {'form': form})

def listar_professor(request):
    professores = Professor.objects.all()
    return render(request, 'crcacad/listas/professor.html', {'professores': professores})

def editar_professor(request, cpf):
    professor = get_object_or_404(Professor, pk=cpf)
    form = ProfessorForm(request.POST or None, instance=professor)
    if form.is_valid():
        form.save()
    return render(request, 'crcacad/forms/formsProfessor.html', {'form': form})

def excluir_professor(request, cpf):

    professor = get_object_or_404(Professor, pk=cpf)
    professor.delete()
    return redirect('crcacad:listar_professor')

def criar_disciplina(request):
    form = DisciplinaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = DisciplinaForm()
    return render(request, 'crcacad/forms/formsDisciplina.html', {'form': form})

def listar_disciplina(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'crcacad/listas/disciplina.html', {'disciplinas': disciplinas})

def editar_disciplina(request, nome):
    disciplina = get_object_or_404(Disciplina, pk=nome)
    form = DisciplinaForm(request.POST or None, instance=disciplina)
    if form.is_valid():
        form.save()
    return render(request, 'crcacad/forms/formsDisciplina.html', {'form': form})

def excluir_disciplina(request, nome):

    disciplina = get_object_or_404(Disciplina, pk=nome)
    disciplina.delete()
    return redirect('crcacad:listar_disciplina')
                    
def criar_atividade(request):
    form = AtividadesForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AtividadesForm()
    return render(request, 'crcacad/forms/formsAtividades.html', {'form': form})

def listar_atividade(request):
    atividades = Atividades.objects.all()
    return render(request, 'crcacad/listas/atividade.html', {'atividades': atividades})

def editar_atividade(request, atividades):
    atividade = get_object_or_404(Atividades, pk=atividades)
    form = AtividadesForm(request.POST or None, instance=atividade)
    if form.is_valid():
        form.save()
    return render(request, 'crcacad/forms/formsAtividades.html', {'form': form})

def excluir_atividade(request, atividades):

    atividade = get_object_or_404(Atividades, pk=atividades)
    atividade.delete()
    return redirect('crcacad:listar_atividade')

def criar_matricula(request):
    form = MatriculaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MatriculaForm()
    return render(request, 'crcacad/forms/formsMatricula.html', {'form': form})

def listar_matricula(request):
    matriculas = Matricula.objects.select_related('aluno', 'turma').all()
    return render(request, 'crcacad/listas/matricula.html', {'matriculas': matriculas})

def editar_matricula(request, aluno_nome):
    matricula = get_object_or_404(Matricula, pk=aluno_nome)
    form = MatriculaForm(request.POST or None, instance=matricula)
    if form.is_valid():
        form.save()
    return render(request, 'crcacad/forms/formsMatricula.html', {'form': form})

def excluir_matricula(request, aluno_nome):

    matricula = get_object_or_404(Matricula, pk=aluno_nome)
    matricula.delete()
    return redirect('crcacad:listar_matricula')
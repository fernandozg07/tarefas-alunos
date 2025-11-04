from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Avg
from .models import Tarefa, Entrega

@login_required
def dashboard(request):
    """Dashboard com estatísticas do sistema"""
    
    if request.user.is_superuser:
        # Estatísticas para Professor
        stats = {
            'total_tarefas': Tarefa.objects.filter(professor=request.user).count(),
            'total_entregas': Entrega.objects.filter(tarefa__professor=request.user).count(),
            'pendentes_avaliacao': Entrega.objects.filter(tarefa__professor=request.user, status='pendente').count(),
            'total_alunos': User.objects.filter(is_superuser=False).count(),
        }
    else:
        # Estatísticas para Aluno
        tarefas_ativas = Tarefa.objects.filter(ativa=True)
        entregas_aluno = Entrega.objects.filter(aluno=request.user)
        
        stats = {
            'tarefas_disponiveis': tarefas_ativas.count(),
            'tarefas_entregues': entregas_aluno.count(),
            'tarefas_pendentes': tarefas_ativas.count() - entregas_aluno.count(),
            'media_notas': entregas_aluno.filter(nota__isnull=False).aggregate(Avg('nota'))['nota__avg'],
        }
    
    return render(request, 'tarefas/dashboard.html', {'stats': stats})
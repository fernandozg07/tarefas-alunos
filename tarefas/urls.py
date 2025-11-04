from django.urls import path
from . import views
from .views_home import home
from .views_dashboard import dashboard
from .views_auth import logout_view
from .views_avaliacao import aprovar_entrega, rejeitar_entrega

# Define o namespace do app para uso em templates (ex: {% url 'tarefas:lista_tarefas' %})
app_name = 'tarefas' 
urlpatterns = [
    # Página inicial
    path('', home, name='home'),
    
    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),
    
    # Logout personalizado
    path('logout/', logout_view, name='logout'),
    
    # Ex: /tarefas/ - Página principal (Lista de Tarefas)
    path('tarefas/', views.lista_tarefas, name='lista_tarefas'), 
    
    # Ex: /tarefas/nova/ - Criar Nova Tarefa (Apenas Professor)
    path('tarefas/nova/', views.criar_tarefa, name='criar_tarefa'),
    
    # Ex: /tarefas/1/entrega/ - Detalhe da Tarefa e Submissão/Revisão
    path('tarefas/<int:tarefa_id>/entrega/', views.detalhe_tarefa_entrega, name='detalhe_tarefa_entrega'),
    
    # Avaliação de entregas
    path('entrega/<int:entrega_id>/aprovar/', aprovar_entrega, name='aprovar_entrega'),
    path('entrega/<int:entrega_id>/rejeitar/', rejeitar_entrega, name='rejeitar_entrega'),
]
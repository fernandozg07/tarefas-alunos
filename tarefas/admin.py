# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import format_html
from .models import Tarefa, Entrega, DesignacaoAluno

# Configuração da exibição do modelo Tarefa no painel de administração
@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    # Campos exibidos na lista de tarefas
    list_display = ('titulo', 'professor', 'data_publicacao', 'data_expiracao', 'ativa', 'is_expired', 'contagem_entregas')
    # Adiciona filtros laterais
    list_filter = ('ativa', 'data_publicacao', 'professor', 'data_expiracao')
    # Campos que podem ser pesquisados
    search_fields = ('titulo', 'descricao', 'professor__username')
    # O professor não precisa preencher o campo 'professor' manualmente
    exclude = ('professor',) 
    
    # Campo personalizado para mostrar a contagem de entregas
    def contagem_entregas(self, obj):
        return obj.entregas.count()
    contagem_entregas.short_description = 'Entregas'

    # Sobrescreve o método save_model para garantir que o professor logado seja o criador
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Se é um novo objeto
            obj.professor = request.user
        super().save_model(request, obj, form, change)


# Configuração da exibição do modelo Entrega no painel de administração
@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'aluno', 'data_entrega', 'status', 'nota', 'arquivo_link', 'atrasada')
    list_filter = ('tarefa', 'aluno', 'data_entrega', 'status', 'nota')
    fields = ('tarefa', 'aluno', 'arquivo', 'status', 'nota', 'comentarios_professor')
    search_fields = ('tarefa__titulo', 'aluno__username', 'observacoes_aluno')
    
    # Adiciona um link para o arquivo no admin
    def arquivo_link(self, obj):
        if obj.arquivo:
            # Garante que o link será exibido corretamente no Admin
            return format_html('<a href="{}" target="_blank">Download</a>', obj.arquivo.url)
        return "Nenhum arquivo"
    arquivo_link.short_description = 'Arquivo'

    # Adiciona um campo booleano para checar atraso
    def atrasada(self, obj):
        if obj.tarefa and obj.data_entrega:
            return obj.data_entrega > obj.tarefa.data_expiracao
        return False
    atrasada.boolean = True
    atrasada.short_description = 'Atrasada'

# Configuração da exibição do modelo Designação no painel de administração
@admin.register(DesignacaoAluno)
class DesignacaoAlunoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'professor', 'data_designacao', 'ativa')
    list_filter = ('professor', 'ativa', 'data_designacao')
    search_fields = ('aluno__username', 'professor__username')
    
    def save_model(self, request, obj, form, change):
        if not obj.pk and request.user.is_superuser:
            obj.professor = request.user
        super().save_model(request, obj, form, change)

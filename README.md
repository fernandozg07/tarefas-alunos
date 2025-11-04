# Sistema de Tarefas Acadêmico

Sistema completo para gerenciamento de tarefas entre professores e alunos, desenvolvido em Django.

## 🚀 Funcionalidades

### Para Professores:
- ✅ Criar e gerenciar tarefas
- ✅ Visualizar todas as entregas dos alunos
- ✅ Definir prazos de entrega
- ✅ Avaliar entregas com notas
- ✅ Painel administrativo completo

### Para Alunos:
- ✅ Visualizar tarefas disponíveis
- ✅ Enviar arquivos para as tarefas
- ✅ Acompanhar status das entregas
- ✅ Visualizar notas recebidas
- ✅ Interface responsiva e moderna

## 🛠️ Tecnologias Utilizadas

- **Backend:** Django 5.0.4
- **Frontend:** HTML5, CSS3, JavaScript, Tailwind CSS
- **Banco de Dados:** SQLite (desenvolvimento)
- **Upload de Arquivos:** Sistema nativo do Django

## 📦 Instalação e Configuração

### 1. Inicialização Automática (Recomendado)
```bash
# Execute o script de inicialização
python iniciar_projeto.py

# Inicie o servidor
python manage.py runserver
```

### 2. Instalação Manual
```bash
# Instalar dependências
pip install -r requirements.txt

# Aplicar migrações
python manage.py makemigrations
python manage.py migrate

# Criar usuários de teste
python manage_users.py

# Iniciar servidor
python manage.py runserver
```

## 👥 Usuários de Teste

### Professor (Superusuário):
- **Usuário:** admin
- **Senha:** admin123

### Alunos:
- **Usuário:** aluno1, aluno2, aluno3
- **Senha:** senha123

## 🌐 Acesso ao Sistema

Após iniciar o servidor, acesse:
- **Sistema:** http://127.0.0.1:8000
- **Admin:** http://127.0.0.1:8000/admin

## 📁 Estrutura do Projeto

```
projeto_faculdade_tarefas/
├── projeto_academico/          # Configurações do Django
├── tarefas/                    # App principal
│   ├── models.py              # Modelos (Tarefa, Entrega)
│   ├── views.py               # Lógica das views
│   ├── forms.py               # Formulários
│   ├── admin.py               # Configuração do admin
│   └── urls.py                # URLs do app
├── templates/                  # Templates HTML
│   ├── base.html              # Template base
│   ├── registration/          # Templates de login
│   └── tarefas/               # Templates do app
├── media/                      # Arquivos enviados pelos alunos
├── manage_users.py            # Script para criar usuários
├── iniciar_projeto.py         # Script de inicialização
└── requirements.txt           # Dependências
```

## 🎯 Como Usar

### Como Professor:
1. Faça login com as credenciais de admin
2. Clique em "Adicionar Nova Tarefa"
3. Preencha título, descrição e prazo
4. Visualize as entregas dos alunos
5. Avalie as entregas no painel admin

### Como Aluno:
1. Faça login com as credenciais de aluno
2. Visualize as tarefas disponíveis
3. Clique em "Detalhes e Envio"
4. Envie seu arquivo
5. Acompanhe sua nota

## 🔧 Personalização

O sistema é totalmente personalizável:
- Modifique os templates em `templates/`
- Ajuste os modelos em `tarefas/models.py`
- Customize as views em `tarefas/views.py`
- Altere estilos no template base

## 📱 Responsividade

Interface totalmente responsiva usando Tailwind CSS, funcionando perfeitamente em:
- 💻 Desktop
- 📱 Mobile
- 📟 Tablet

## 🎨 Design

- Interface moderna e limpa
- Cores consistentes (azul/índigo)
- Feedback visual para ações
- Mensagens de sucesso/erro
- Animações suaves

## 🔒 Segurança

- Autenticação obrigatória
- Separação de permissões (Professor/Aluno)
- Validação de formulários
- Proteção CSRF
- Upload seguro de arquivos

## 📈 Próximas Melhorias

- [ ] Sistema de comentários nas entregas
- [ ] Notificações por email
- [ ] Relatórios de desempenho
- [ ] API REST
- [ ] Integração com calendário

---

**Desenvolvido para fins educacionais** 🎓
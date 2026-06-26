# Demo Django — Parte 2

Continuação do projeto `demo-django`. Nesta parte foram adicionados novos campos ao modelo, uma nova página `/sobre/` e mudanças no visual.

## Tecnologias

- Python 3.12
- Django 5.1.3
- Tailwind CSS (CDN)
- Docker + Docker Compose
- SQLite

## O que foi adicionado nesta parte

- Campo `autor` no modelo `Mensagem`
- Nova página `/sobre/` com view, rota e template próprios
- Link `/sobre` no menu de navegação
- Visual atualizado com novo gradiente de cores

## Estrutura do projeto

```
demo-django/
├── core/               # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── home/               # App principal
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── 0002_mensagem_autor.py
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/
│   └── home/
│       ├── index.html
│       └── sobre.html
├── docker-compose.yml
├── Dockerfile
├── manage.py
└── requirements.txt
```

## Como executar

### Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) instalado

### Subir o projeto

```bash
docker compose up --build
```

Acesse: [http://localhost:8000](http://localhost:8000)

### Parar o projeto

```bash
docker compose down
```

## Funcionalidades

- Página inicial listando mensagens com título, conteúdo, autor e data
- Página `/sobre/` com informações do projeto
- Painel administrativo em `/admin/`
- Navegação entre páginas no menu

## Criar usuário admin

Com o servidor rodando, em outro terminal:

```bash
docker compose exec web python manage.py createsuperuser
```

## Fluxo MTV (Model–Template–View)

```
Navegador
   ↓
core/urls.py     → encaminha para o app home
   ↓
home/urls.py     → encaminha para a view correta
   ↓
home/views.py    → consulta o banco via models.py
   ↓
home/models.py   → ORM converte para SQL no SQLite
   ↓
templates/home/  → renderiza o HTML com os dados
   ↓
HTML pronto      → navegador exibe a página
```

## Branch

Este código corresponde ao branch `bcc481-django-parte2`.

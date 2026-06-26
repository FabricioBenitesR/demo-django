# Demo Django — Parte 1

Site simples construído com **Django**, estilizado com **Tailwind CSS** via CDN, com banco de dados **SQLite** e executado em container **Docker**.

## Tecnologias

- Python 3.12
- Django 5.1.3
- Tailwind CSS (CDN)
- Docker + Docker Compose
- SQLite

## Estrutura do projeto

```
demo-django/
├── core/               # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── home/               # App principal
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/
│   └── home/
│       └── index.html
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

- Página inicial que lista mensagens cadastradas no banco de dados
- Painel administrativo do Django em `/admin/`
- Modelo `Mensagem` com título, conteúdo e data de criação

## Criar usuário admin

Com o servidor rodando, em outro terminal:

```bash
docker compose exec web python manage.py createsuperuser
```

Acesse `/admin/` para cadastrar mensagens que aparecerão na página inicial.

## Branch

Este código corresponde ao branch `bcc481-django-parte1`.

# demo-django

Projeto de demonstração desenvolvido na disciplina de **Programação Web**, utilizando **Django**, **Tailwind CSS** (via CDN) e **Docker Compose**, com banco de dados **SQLite** local.

O objetivo do projeto é evoluir, passo a passo, uma aplicação Django simples até implementar o ciclo completo de **CRUD** (Create, Read, Update, Delete) sobre um model de mensagens.

## Tecnologias

- [Django](https://www.djangoproject.com/) 5.1
- [Tailwind CSS](https://tailwindcss.com/) (via CDN)
- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/)
- SQLite

## Como executar o projeto

Com o Docker instalado, execute:

```bash
docker compose up --build
```

Acesse a aplicação em:

```
http://localhost:8000
```

Para acessar o painel administrativo do Django:

```
http://localhost:8000/admin/
```

Para parar o projeto:

```bash
Ctrl+C
docker compose down
```

## Funcionalidades

- **Página inicial**: lista todas as mensagens cadastradas, exibindo título, conteúdo, autor, categoria e tags.
- **Página "Sobre"**: informações sobre o projeto.
- **Painel administrativo**: gerenciamento completo dos dados (`Mensagem`, `Categoria`, `Tag`) via `/admin/`.
- **Cadastro de mensagens pelo visitante** (`/nova/`): formulário público para criar novas mensagens, com seleção de categoria e criação de tags a partir de texto digitado.

## Estrutura do model

- **Mensagem**: `titulo`, `conteudo`, `autor`, `categoria` (`ForeignKey`), `tags` (`ManyToManyField`), `criada_em` (preenchido automaticamente).
- **Categoria**: usada para classificar as mensagens.
- **Tag**: criada automaticamente a partir do texto digitado pelo visitante no formulário de nova mensagem.

## Evolução do projeto (roteiro)

O projeto foi construído em etapas, cada uma correspondendo a uma branch/entrega:

| Parte | Conteúdo |
| ----- | -------- |
| 1     | Estrutura inicial do projeto Django + Docker + Tailwind |
| 2     | Model `Mensagem` e listagem de dados na página inicial |
| 3     | Relacionamento `ForeignKey` com `Categoria` |
| 4     | Relacionamento `ManyToManyField` com `Tag` |
| 5     | Formulário público (`ModelForm`) para criação de mensagens — implementação do **C** (Create) do CRUD, com proteção CSRF e padrão Post/Redirect/Get |

### Parte 5 — Formulário e Create do CRUD

Nesta etapa foi implementado:

- `home/forms.py`: `MensagemForm`, um `ModelForm` baseado no model `Mensagem`, com campo extra `tags` (texto livre separado por vírgula).
- `home/views.py`: view `nova_mensagem`, que trata requisições **GET** (exibe o formulário) e **POST** (valida, salva a mensagem e associa as tags, criando-as automaticamente via `get_or_create`).
- `home/urls.py`: rota `/nova/` associada à view `nova_mensagem`.
- `templates/home/nova.html`: template do formulário, com proteção `{% csrf_token %}`.
- `templates/home/index.html`: botão **+ Nova mensagem** para acesso ao formulário.

## Testando o CRUD (Create)

1. Acesse `http://localhost:8000/` e clique em **+ Nova mensagem**.
2. Preencha título, conteúdo, autor, categoria e tags (separadas por vírgula).
3. Clique em **Publicar**.
4. Você será redirecionado à página inicial, onde a nova mensagem aparecerá no topo da lista.

## Próximos passos

Nas próximas partes do roteiro serão implementados o **U** (Update) e o **D** (Delete) do CRUD, permitindo editar e apagar mensagens existentes diretamente pela interface pública.

---

Projeto desenvolvido para fins didáticos na disciplina de Programação Web.

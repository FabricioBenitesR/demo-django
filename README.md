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
- **Criar mensagem** (`/nova/`): formulário público para publicar novas mensagens, com seleção de categoria e criação de tags a partir de texto digitado.
- **Editar mensagem** (`/mensagens/<id>/editar/`): formulário reaproveitado para atualizar uma mensagem já existente, incluindo suas tags.
- **Remover mensagem** (`/mensagens/<id>/remover/`): página de confirmação antes da exclusão definitiva.

O ciclo **CRUD** está completo: qualquer visitante pode **criar**, **listar**, **editar** e **remover** mensagens diretamente pela interface pública, sem precisar abrir o painel admin.

## Estrutura do model

- **Mensagem**: `titulo`, `conteudo`, `autor`, `categoria` (`ForeignKey`), `tags` (`ManyToManyField`), `criada_em` (preenchido automaticamente).
- **Categoria**: usada para classificar as mensagens.
- **Tag**: criada automaticamente a partir do texto digitado pelo visitante nos formulários de criação/edição.

## Evolução do projeto (roteiro)

O projeto foi construído em etapas, cada uma correspondendo a uma branch/entrega:

| Parte | Conteúdo |
| ----- | -------- |
| 1     | Estrutura inicial do projeto Django + Docker + Tailwind |
| 2     | Model `Mensagem` e listagem de dados na página inicial |
| 3     | Relacionamento `ForeignKey` com `Categoria` |
| 4     | Relacionamento `ManyToManyField` com `Tag` |
| 5     | Formulário público (`ModelForm`) para criação de mensagens — **C** (Create) do CRUD, com proteção CSRF e padrão Post/Redirect/Get |
| 6     | Edição e remoção de mensagens — **U** (Update) e **D** (Delete) do CRUD, finalizando o ciclo completo |

### Parte 5 — Formulário e Create do CRUD

- `home/forms.py`: `MensagemForm`, um `ModelForm` baseado no model `Mensagem`, com campo extra `tags` (texto livre separado por vírgula).
- View `nova_mensagem`: trata requisições **GET** (exibe o formulário) e **POST** (valida, salva a mensagem e associa as tags, criando-as automaticamente via `get_or_create`).
- Rota `/nova/` e template `templates/home/nova.html`, protegido com `{% csrf_token %}`.
- Botão **+ Nova mensagem** na página inicial.

### Parte 6 — Editar e remover: finalizando o ciclo CRUD

- **`_aplicar_tags(mensagem, tags_texto)`**: função extraída em `home/views.py` para reaproveitar a lógica de processamento das tags entre criação e edição (princípio DRY).
- **Editar (`Update`)**:
  - View `editar_mensagem(request, id)`: usa `get_object_or_404` para buscar a mensagem e reaproveita o `MensagemForm` passando `instance=mensagem`, atualizando o registro em vez de criar um novo.
  - No GET, o formulário vem preenchido com os dados atuais, incluindo as tags já cadastradas.
  - Rota: `mensagens/<int:id>/editar/`.
  - Template: `templates/home/editar.html`.
- **Remover (`Delete`)**:
  - View `remover_mensagem(request, id)`: no GET exibe uma página de confirmação; a exclusão de fato só ocorre no **POST**, protegida por `{% csrf_token %}` — nunca via GET, para evitar exclusões acidentais.
  - Rota: `mensagens/<int:id>/remover/`.
  - Template: `templates/home/remover.html`, com opções **"Sim, remover"** (POST) e **"Cancelar"** (link simples).
- Botões **editar** e **remover** adicionados a cada mensagem na página inicial (`templates/home/index.html`).
- Mensagens de retorno (*flash messages*) exibidas após criar, editar ou remover, usando `django.contrib.messages`.

## Testando o ciclo CRUD completo

Com o projeto rodando (`docker compose up`), é possível percorrer todo o ciclo pela interface, sem abrir o admin:

1. **Create** — clique em **+ Nova mensagem**, preencha e publique. Ela aparece no topo da lista.
2. **Read** — confira que a mensagem aparece com título, categoria e tags.
3. **Update** — clique em **editar**. O formulário abre já preenchido, inclusive com as tags. Altere o título, remova uma tag e salve — confirme que a alteração aparece na lista.
4. **Delete** — clique em **remover**. Na página de confirmação, teste **Cancelar** (nada acontece) e depois **Sim, remover** (a mensagem some da lista).

Casos de borda:

- Acessar uma URL inexistente, como `http://localhost:8000/mensagens/9999/editar/`, deve retornar a página **404** (via `get_object_or_404`).
- Editar uma mensagem deixando o título em branco deve recarregar o formulário com erro de validação, sem salvar.

## Conceitos exercitados

- **Models** e relacionamentos (`ForeignKey`, `ManyToManyField`).
- **Migrations** para evoluir o banco de dados.
- **Forms** (`ModelForm`) para validar e reaproveitar entrada de dados entre criação e edição.
- **Views** que respondem a `GET` e `POST`.
- **Parâmetros de rota** (`<int:id>`) para identificar registros específicos na URL.
- **`get_object_or_404`** para buscas seguras.
- Padrão **Post/Redirect/Get (PRG)** e proteção **CSRF**.
- Templates reaproveitáveis com a linguagem de templates do Django.

---

Projeto desenvolvido para fins didáticos na disciplina de Programação Web.

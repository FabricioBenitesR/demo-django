# demo-django — Parte 6: Editar e remover (finalizando o ciclo CRUD)

Esta etapa do projeto `demo-django` implementa o **U** (Update) e o **D** (Delete) do CRUD, completando o ciclo iniciado na parte 5 (que trouxe o **C** de Create). Agora o visitante consegue **criar**, **listar**, **editar** e **remover** mensagens direto pela interface pública, sem precisar abrir o painel admin.

## Tecnologias

- [Django](https://www.djangoproject.com/) 5.1
- [Tailwind CSS](https://tailwindcss.com/) (via CDN)
- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/)
- SQLite

## Como executar o projeto

```bash
docker compose up --build
```

Acesse em:

```
http://localhost:8000
```

Para parar:

```bash
Ctrl+C
docker compose down
```

> **Pré-requisito:** esta parte pressupõe que a parte 5 já foi concluída, com o `MensagemForm` (`home/forms.py`), a view `nova_mensagem`, a rota `nova/` e o template `home/nova.html` funcionando.

## O que foi implementado

### 1. Função `_aplicar_tags` (princípio DRY)

Em `home/views.py`, a lógica de transformar o texto de tags em objetos `Tag` foi extraída para uma função reutilizável, evitando duplicar código entre criação e edição:

```python
def _aplicar_tags(mensagem, tags_texto):
    """Substitui as tags da mensagem pelas que vieram do formulário."""
    mensagem.tags.clear()
    for pedaco in tags_texto.split(","):
        nome = slugify(pedaco)
        if nome:
            tag, _ = Tag.objects.get_or_create(nome=nome)
            mensagem.tags.add(tag)
```

O `mensagem.tags.clear()` é essencial na edição: sem ele, editar uma mensagem só acrescentaria tags, nunca removeria as que o usuário apagou do campo.

### 2. Editar mensagem (Update)

- **View** `editar_mensagem(request, id)`: usa `get_object_or_404` para buscar a mensagem pelo `id` (retorna 404 automaticamente se não existir) e reaproveita o `MensagemForm`, passando `instance=mensagem`. No GET, o formulário vem pré-preenchido com os dados atuais, incluindo as tags já cadastradas (montadas via `initial={"tags": tags_atuais}`). No POST, `form.save()` faz um `UPDATE` em vez de um `INSERT`.
- **Rota**: `mensagens/<int:id>/editar/` — o `<int:id>` é um *path converter* que captura o número da URL e o entrega à view.
- **Template**: `templates/home/editar.html`, praticamente idêntico ao `nova.html`, mudando o título, o texto do botão e o `action` do formulário para `{% url 'editar_mensagem' mensagem.id %}`.

### 3. Remover mensagem (Delete)

- **View** `remover_mensagem(request, id)`: no **GET**, apenas exibe uma página de confirmação. A exclusão só acontece no **POST** (protegido por `{% csrf_token %}`) — nunca no GET, para evitar que robôs de busca, pré-carregamento do navegador ou antivírus apaguem registros sem intenção do usuário.
- **Rota**: `mensagens/<int:id>/remover/`.
- **Template**: `templates/home/remover.html`, com um botão **"Sim, remover"** dentro de um `<form method="post">` e um link **"Cancelar"** (`<a href="/">`) que volta para a home sem apagar nada.

### 4. Botões na listagem

Em `templates/home/index.html`, cada mensagem da lista agora exibe os links **editar** e **remover**, montados com `{% url 'editar_mensagem' m.id %}` e `{% url 'remover_mensagem' m.id %}`.

## Arquivos alterados/criados nesta parte

- `home/views.py` — função `_aplicar_tags`, views `editar_mensagem` e `remover_mensagem`
- `home/urls.py` — rotas `mensagens/<int:id>/editar/` e `mensagens/<int:id>/remover/`
- `templates/home/editar.html` — novo
- `templates/home/remover.html` — novo
- `templates/home/index.html` — links de editar/remover em cada mensagem

## Testando o ciclo CRUD completo

1. **Create** — clique em **+ Nova mensagem**, preencha e publique.
2. **Read** — confira que a mensagem aparece na lista com título, categoria e tags.
3. **Update** — clique em **editar**; o formulário abre já preenchido, inclusive as tags. Altere o título, remova uma tag e salve.
4. **Delete** — clique em **remover**; teste **Cancelar** (nada acontece) e depois **Sim, remover** (a mensagem desaparece da lista).

Casos de borda:

- `http://localhost:8000/mensagens/9999/editar/` deve retornar página **404**, graças ao `get_object_or_404`.
- Editar deixando o título em branco deve recarregar o formulário com erro de validação, sem salvar nada.

## Conceitos exercitados

- Parâmetros de rota (`<int:id>`)
- `get_object_or_404`
- Reaproveitamento de `ModelForm` com `instance`
- Padrão de exclusão via POST (nunca via GET)
- Princípio DRY com função auxiliar
- Flash messages (`django.contrib.messages`)

---

Projeto desenvolvido para fins didáticos na disciplina de Programação Web.

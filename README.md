# Demo Django — Parte 4

Branch: `bcc481-django-parte4`

## O que foi feito nesta parte

Nesta etapa foi criado um novo modelo (`Tag`) e uma relação **muitos-para-muitos (N:N)** entre `Tag` e `Mensagem`, usando `ManyToManyField` do Django. Essa parte continua o trabalho da [parte 3](https://github.com/FabricioBenitesR/demo-django/tree/bcc481-django-parte3), onde foi criado o modelo `Categoria` (relação 1:N).

### 1. Novo modelo `Tag`

Adicionado em `home/models.py`:

```python
class Tag(models.Model):
    nome = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome
```

### 2. Relação com `Mensagem`

O modelo `Mensagem` recebeu um novo campo `tags`:

```python
tags = models.ManyToManyField(Tag, blank=True, related_name="mensagens")
```

- Diferente do `ForeignKey` (1:N), o `ManyToManyField` permite que **uma mensagem tenha várias tags** e **uma tag esteja em várias mensagens**.
- Por trás, o Django cria uma tabela intermediária (`home_mensagem_tags`) para guardar essa relação.
- `blank=True`: permite mensagens sem nenhuma tag.
- `related_name="mensagens"`: permite acessar as mensagens de uma tag com `tag.mensagens.all()`.

### 3. Admin

`Tag` foi registrada no Django admin (`home/admin.py`), com listagem e busca por nome. O admin de `Mensagem` passou a:

- Filtrar por `tags` além de `categoria`.
- Usar `filter_horizontal = ("tags",)`, que exibe um widget de duas colunas para selecionar múltiplas tags mais facilmente.

### 4. Migrations

Foram geradas e aplicadas as migrations para criar a tabela `Tag` e a tabela intermediária da relação N:N:

```bash
docker compose run --rm web python manage.py makemigrations
docker compose run --rm web python manage.py migrate
```

Migration gerada: `home/migrations/0004_tag_mensagem_tags.py`.

### 5. Template

O template `templates/home/index.html` foi atualizado para exibir as tags de cada mensagem (quando existirem), logo abaixo da categoria, no formato `#tag`.

## Como executar o projeto

```bash
docker compose up --build
```

Acesse `http://localhost:8000` e o admin em `http://localhost:8000/admin/`.

Para parar:

```bash
docker compose down
```

## Link da Parte 4

https://github.com/FabricioBenitesR/demo-django/tree/bcc481-django-parte4

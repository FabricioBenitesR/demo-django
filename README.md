# Demo Django — Parte 3

Branch: `bcc481-django-parte3`

## O que foi feito nesta parte

Nesta etapa do projeto foi criado um novo modelo (`Categoria`) e uma relação **um-para-muitos (1:N)** entre `Categoria` e `Mensagem`, usando `ForeignKey` do Django.

### 1. Novo modelo `Categoria`

Adicionado em `home/models.py`:

```python
class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome
```

### 2. Relação com `Mensagem`

O modelo `Mensagem` recebeu um novo campo `categoria`:

```python
categoria = models.ForeignKey(
    Categoria,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="mensagens",
)
```

- `on_delete=models.SET_NULL`: se uma categoria for excluída, as mensagens ligadas a ela não são apagadas, apenas o campo `categoria` fica `NULL`.
- `null=True, blank=True`: permite mensagens sem categoria.
- `related_name="mensagens"`: permite acessar as mensagens de uma categoria com `categoria.mensagens.all()`.

### 3. Admin

`Categoria` foi registrada no Django admin (`home/admin.py`), com listagem e busca por nome. O admin de `Mensagem` passou a mostrar e filtrar por categoria.

### 4. Migrations

Foram geradas e aplicadas as migrations para criar a tabela `home_categoria` e adicionar a coluna `categoria_id` em `home_mensagem`:

```bash
docker compose run --rm web python manage.py makemigrations
docker compose run --rm web python manage.py migrate
```

### 5. Template

O template `templates/home/index.html` foi atualizado para exibir a categoria de cada mensagem (quando existir), usando `{{ m.categoria.nome }}`.

### 6. Relação inversa

Graças ao `related_name="mensagens"`, é possível navegar da categoria para as mensagens:

```python
from home.models import Categoria
c = Categoria.objects.get(nome="Aviso")
c.mensagens.all()
```

## Como executar o projeto

```bash
docker compose up --build
```

Acesse `http://localhost:8000` e o admin em `http://localhost:8000/admin/`.

Para parar:

```bash
docker compose down
```

## Link da Parte 3

https://github.com/FabricioBenitesR/demo-django/tree/bcc481-django-parte3

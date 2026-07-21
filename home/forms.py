from django import forms

from .models import Mensagem

INPUT = (
    "w-full rounded-lg bg-slate-800 border border-white/10 px-3 py-2 "
    "text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-400"
)

class MensagemForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        label="Tags",
        help_text="Separe por vírgula. Ex.: django, tutorial, iniciante",
        widget=forms.TextInput(attrs={"class": INPUT}),
    )

    class Meta:
        model = Mensagem
        fields = ["titulo", "conteudo", "autor", "categoria"]
        labels = {
            "titulo": "Título",
            "conteudo": "Conteúdo",
            "autor": "Autor",
            "categoria": "Categoria",
        }
        widgets = {
            "titulo": forms.TextInput(attrs={"class": INPUT}),
            "conteudo": forms.Textarea(attrs={"class": INPUT, "rows": 4}),
            "autor": forms.TextInput(attrs={"class": INPUT}),
            "categoria": forms.Select(attrs={"class": INPUT}),
        }

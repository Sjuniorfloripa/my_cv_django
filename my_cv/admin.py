from django.contrib import admin
from .models import DadosPessoais, Experiencia, Formacao, Habilidade, Projeto, Idioma

admin.site.register(DadosPessoais)
admin.site.register(Experiencia)
admin.site.register(Formacao)
admin.site.register(Habilidade)
admin.site.register(Idioma)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'link_repositorio', 'link_demo', 'data_publicacao')
    filter_horizontal = ('tecnologias',)

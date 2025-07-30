from django.shortcuts import render
from .models import DadosPessoais, Experiencia, Formacao, Habilidade, Projeto, Idioma

def curriculo_view(request):
    dados_pessoais = DadosPessoais.objects.first()
    experiencias = Experiencia.objects.all().order_by('-periodo_inicio')
    formacoes = Formacao.objects.all().order_by('-ano_conclusao')
    habilidades = Habilidade.objects.all().order_by('categoria', '-nivel')
    categorias_habilidades = Habilidade.objects.values_list('categoria', flat=True).distinct()
    projetos = Projeto.objects.all().order_by('-data_publicacao')
    idiomas = Idioma.objects.all()

    context = {
        'dados': dados_pessoais,
        'experiencias': experiencias,
        'formacoes': formacoes,
        'habilidades': habilidades,
        'categorias_habilidades': categorias_habilidades,
        'projetos': projetos,
        'idiomas': idiomas,
    }

    return render(request, 'home.html', context)

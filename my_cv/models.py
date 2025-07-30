from django.db import models


class DadosPessoais(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    cargo_atual = models.CharField(max_length=100)
    resumo_profissional = models.TextField()
    linkedin = models.URLField()
    github = models.URLField()
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

class Experiencia(models.Model):
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    periodo_inicio = models.DateField()
    periodo_fim = models.DateField(null=True, blank=True)
    atual = models.BooleanField(default=False)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.cargo} na {self.empresa}"

class Formacao(models.Model):
    NIVEIS = [('Graduação', 'Graduação'), ('Pós-Graduação', 'Pós-Graduação'), ('Técnico', 'Técnico'), ('Curso Livre', 'Curso Livre')]
    STATUS = [('Completo', 'Completo'), ('Em andamento', 'Em andamento'), ('Trancado', 'Trancado')]

    instituicao = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20, choices=NIVEIS)
    ano_conclusao = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return f"{self.curso} ({self.status})"

class Habilidade(models.Model):
    NIVEIS = [('Básico', 'Básico'), ('Intermediário', 'Intermediário'), ('Avançado', 'Avançado')]
    CATEGORIAS = [('Back-end', 'Back-end'), ('Front-end', 'Front-end'), ('Fullstack', 'Fullstack'),
                  ('DevOps', 'DevOps'), ('Banco de Dados', 'Banco de Dados'), ('Cloud', 'Cloud'), ('Outros', 'Outros')]

    nome = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20, choices=NIVEIS)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)

    def __str__(self):
        return f"{self.nome} ({self.nivel})"

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    link_repositorio = models.URLField(blank=True)
    link_demo = models.URLField(blank=True)
    tecnologias = models.ManyToManyField('Habilidade', related_name='projetos')
    data_publicacao = models.DateField()

    def __str__(self):
        return self.titulo

class Idioma(models.Model):
    NIVEIS = [('Básico', 'Básico'), ('Intermediário', 'Intermediário'), ('Avançado', 'Avançado'), ('Fluente', 'Fluente'), ('Nativo', 'Nativo')]

    nome = models.CharField(max_length=50)
    nivel = models.CharField(max_length=20, choices=NIVEIS)

    def __str__(self):
        return f"{self.nome} ({self.nivel})"

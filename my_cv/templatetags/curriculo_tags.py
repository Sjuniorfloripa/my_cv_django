from django import template

register = template.Library()

@register.filter
def categoria_cor(value):
    cores = {
        'Back-end': 'bg-primary',
        'Front-end': 'bg-success',
        'Fullstack': 'bg-info',
        'DevOps': 'bg-warning text-dark',
        'Banco de Dados': 'bg-secondary',
        'Cloud': 'bg-dark',
        'Outros': 'bg-light text-dark',
    }
    return cores.get(value, 'bg-secondary')

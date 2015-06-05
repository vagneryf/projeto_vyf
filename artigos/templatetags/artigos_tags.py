from django import template 
from artigos.models import Artigo

register = template.Library()

@register.inclusion_tag('artigos/lista_artigos.html')
def lista_artigos(code=None):
    lista_artigos = None
    try:
        lista_artigos = Artigo.objects.all().only('id', 'publicacao', 'titulo', 'categoria')[:6]
    except Exception, e:
        pass
    return {'lista_artigos':lista_artigos,}
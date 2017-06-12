from django import template
from slider.models import IndexSlide

register = template.Library()

@register.inclusion_tag("index_header_slider.html")
def index_header_slider():
    #slider = Slider.objects.filter(id=1)
    sliders = IndexSlide.objects.all()
    return {'sliders': sliders}

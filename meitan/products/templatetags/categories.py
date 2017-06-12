from django import template
from products.models import Category

register = template.Library()

@register.inclusion_tag("categories.html")
def show_categories():
    categories = Category.get_main_categories()
    print categories
    return {'categories': categories}

@register.inclusion_tag("categories_footer.html")
def show_categories_footer():
    categories = Category.get_main_categories()
    print categories
    return {'categories': categories}



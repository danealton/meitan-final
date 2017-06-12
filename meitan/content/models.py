# from django.db import models
from feincms.module.page.models import Page
from django.utils.translation import ugettext_lazy as _
from .content_types import ProductsNewCT
from .content_types import ProductsRelated
from .content_types import NewsBlock
from feincms.content.application.models import ApplicationContent
from django.db import models

# Create your models here.

Page.register_extensions(
    'feincms.extensions.changedate',
    'feincms.extensions.translations',
    'feincms.module.page.extensions.navigation',
    'feincms.module.page.extensions.navigationgroups',
    'feincms.extensions.seo',
    'feincms.module.page.extensions.titles'
)  # Example set of extensions



Page.register_templates({
    'title': _('Page'),
    'path': 'content/pages/page.html',
    'regions': (
        ('main', _('Main content area')),
    ),
})


Page.register_templates({
    'title': _('Page Index'),
    'path': 'content/pages/page_index.html',
    'regions': (
        ('main', _('Main content area')),
    ),
})





Page.create_content_type(ApplicationContent, APPLICATIONS=(
    ('products.urls', 'Product application'),
    ('cart.urls', 'Cart application'),
    ('sales.urls', 'Sales application')
))


Page.create_content_type(ProductsNewCT)
Page.create_content_type(ProductsRelated)
Page.create_content_type(NewsBlock)

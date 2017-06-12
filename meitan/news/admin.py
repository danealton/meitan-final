# Register your models here.
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import News
from django.utils.translation import ugettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin
from common.admin import  CommonPostAdmin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
#from .form import NewMediaForm

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

    fieldsets = (
        (_('Article'), {

           'fields': ('title','text', 'text_preview', 'image', 'date',),
       }),
    )


admin.site.register(News, NewsAdmin)

# Register your models here.

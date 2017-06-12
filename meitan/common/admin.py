from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html
from modeltranslation.admin import TabbedTranslationAdmin
from adminsortable2.admin import SortableAdminMixin
from django_mptt_admin.admin import DjangoMpttAdmin


def admin_thumbnail_img(obj):
    return format_html('<img src=%s >' % obj.get_admin_thumbnail())


class CategoryAdmin(DjangoMpttAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'title_ru', )
    #list_filter = ('category',)
    #search_fields = ('title_ru', 'category')


class CommonPostAdmin(SortableAdminMixin, TabbedTranslationAdmin):
    list_display = ('title_ru','text_preview', 'created_at')
    date_hierarchy = 'created_at'
    sortable = 'order'

    def admin_thumbnail_img(obj):
    	return format_html('<img src=%s >' % obj.get_admin_thumbnail())






# class FoodDrinksAdmin(GridAdmin):
#     list_display = ('title_en', admin_thumbnail_img, 'position', 'created_at')
#     date_hierarchy = 'created_at'
#
# class ArticleAdmin(GridAdmin):
#     fieldsets = (
#         (_('Cover'), {
#             'fields': ('title', 'grid_cover', 'grid_text',),
#         }),
#         (_('Article'), {
#             'fields': ('article_title', 'article_subtitle', 'article_text', 'article_image', 'article_date',),
#         }),
#     )

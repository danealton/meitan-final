from modeltranslation.translator import translator, TranslationOptions


class CommonPostTranslationOptions(TranslationOptions):
    fields = ('title','subtitle', 'text','text_preview',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', )


from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Form)
class FormTranslate(TranslationOptions):
    fields = ("title", "message")
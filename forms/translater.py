from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Form)
class FormTranslate(TranslationOptions):
    fields = ("title", "message")
    fallback_undefined ={
        "title": "--this was not translated--",
        "message":"--this was not translated--"
    }
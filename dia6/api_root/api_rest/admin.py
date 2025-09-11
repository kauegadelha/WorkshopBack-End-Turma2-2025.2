from django.contrib import admin

# Register your models here.
from .models import Endereco
class EnderecoAdmin (admin.ModelAdmin):
    search_fields = [
        "cep"
    ]
admin.site.register(Endereco, EnderecoAdmin)

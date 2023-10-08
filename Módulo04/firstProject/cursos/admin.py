from django.contrib import admin

from .models import Lista_curso, Docente, WebDocente

# Register your models here.

admin.site.register(Lista_curso)
admin.site.register(Docente)
admin.site.register(WebDocente)
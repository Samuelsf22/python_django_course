from django.contrib import admin
from django.urls import path, include, utils


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cursos.urls')),
]

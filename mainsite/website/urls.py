from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #Mainapp index olarak kullanılmakta!
    #path("mainapp/", include("mainapp.urls")),
    path("", include("mainapp.urls")),
    path("admin/", admin.site.urls),
]
from django.contrib import admin
from django.urls import path, include
from api.views import home

urlpatterns = [
    path("", home, name="home"),                 # root URL
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
]


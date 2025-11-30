from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# DRF router
router = DefaultRouter()
router.register(r"books", BookViewSet, basename="book")

urlpatterns = [
    # For the earlier ListAPIView task
    path("books/", BookList.as_view(), name="book-list"),

    # Router-generated routes: /books/, /books/<pk>/
    path("", include(router.urls)),
]


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books.api.viewsets import BooksViewset

route = routers.DefaultRouter()
route.register(r'books', BooksViewset, basename='Books')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]

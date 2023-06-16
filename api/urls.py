from django.urls import path
from api import views

urlpatterns = [
    path("products/", views.ProductAPIView.as_view({"get": "list", "post": "create"})),
    path("products/<int:id>/", views.ProductAPIView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path("category/", views.CategoryAPIView.as_view({"get": "list", "post": "create"})),
    path("category/<int:id>/", views.CategoryAPIView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

]
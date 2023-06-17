from django.urls import path
from api import views

urlpatterns = [
    path("products/", views.ProductAPIView.as_view()),
    path("products/<int:id>/", views.ProductDetailAPIView.as_view()),
    path("category/", views.CategoryAPIView.as_view()),
    path("category/<int:id>/", views.CategoryDetailAPIView.as_view()),

]
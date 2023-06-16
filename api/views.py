from rest_framework.viewsets import ModelViewSet
from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.


class ProductAPIView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"


class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"

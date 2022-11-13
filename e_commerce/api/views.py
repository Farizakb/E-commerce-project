from multiprocessing import context
from django.http import JsonResponse
from product.models import Product,Category
from .serializers import CategorySerailizer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly,IsAdminUser


class CategoryApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerailizer
    permission_classes = (IsAuthenticatedOrReadOnly,)
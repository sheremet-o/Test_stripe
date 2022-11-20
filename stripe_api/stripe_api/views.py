from rest_framework import viewsets

from items.models import Item
from .serializers import ItemSerializer


class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
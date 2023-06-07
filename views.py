from rest_framework import viewsets

# import local data
from .serializers import AnkitSerializer
from .models import AnkitModel


# create a viewset
class GeeksViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = AnkitModel.objects.all()

    # specify serializer to be used
    serializer_class = AnkitSerializer
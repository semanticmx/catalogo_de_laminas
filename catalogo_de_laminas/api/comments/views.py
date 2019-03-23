from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from catalogo_de_laminas.wised import models as wised_models
from catalogo_de_laminas.api.comments import serializers as comments_serializer


class WpCommentsViewSet(viewsets.ModelViewSet):
    queryset = wised_models.Wp2Popularpostsdata.objects.all().order_by('-pageviews')
    serializer_class = comments_serializer.WpCommentsSerializer
    permission_classes = (IsAdminUser,)


class WpCommentsAddView(generics.CreateAPIView):
    queryset = wised_models.Wp2Popularpostsdata.objects.all().order_by('-pageviews')
    serializer_class = comments_serializer.WpCommentsSerializer
    permission_classes = (IsAdminUser,)

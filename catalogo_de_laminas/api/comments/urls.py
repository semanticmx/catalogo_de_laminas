from django.urls import include, path

from rest_framework import routers

from catalogo_de_laminas.api.comments.views import (
    WpCommentsViewSet,
    WpCommentsAddView,
)

app_name = 'comments'

router = routers.DefaultRouter()
router.register(r'', WpCommentsViewSet)

urlpatterns = [
    # /api/comments/add/
    path('add/', WpCommentsAddView.as_view(), name='add'),
    # /api/comments/...
    path('', include(router.urls)),
]

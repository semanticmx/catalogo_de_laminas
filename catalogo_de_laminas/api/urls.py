from django.urls import include, path

app_name = 'api'

urlpatterns = [
    path('comments/', include('catalogo_de_laminas.api.comments.urls', namespace='comments'))
]

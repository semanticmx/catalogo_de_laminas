from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from catalogo_de_laminas.wised import models as wised_models

admin.site.register(wised_models.WpBlogs)
admin.site.register(wised_models.WpComments)

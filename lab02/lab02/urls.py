from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('encuesta/', include('encuesta.urls')),
    path('operacion/', include('seramio.urls')),
    path('admin/', admin.site.urls),
]

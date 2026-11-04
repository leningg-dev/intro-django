
from django.contrib import admin
from django.urls import path, include 

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    #el namespace es lo que se manda a llamar en el html para hacer dirección ahí
    path('blog/', include('blog.urls', namespace='blog') )
]

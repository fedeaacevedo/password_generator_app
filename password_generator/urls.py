
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from generator import views

urlpatterns = [
   # path('admin/', admin.site.urls),
   path('', views.home),
   path('about', views.about),
   path('password', views.password, name='password')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# 
from django.contrib import admin
from django.urls import path,  include 
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('admin/', admin.site.urls),
    path('administration/',include('administration.urls') ),
    path('account/', include('account.urls')),
    path('voting/', include('voting.urls')),
    path('api/', include('api.urls')),
    
]+ static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

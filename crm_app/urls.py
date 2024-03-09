from .import views
from django.urls import path


urlpatterns = [
    path('',views.home,name=''),
    path('archive',views.archive,name='archive'),
    path('dash',views.dash,name='dash'),
   
]
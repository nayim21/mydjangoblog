from django.contrib import admin
from django.urls import path , include
from django.urls import  include

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about),
    path('',views.home),
    path('articles/' , include('articles.urls')),
]

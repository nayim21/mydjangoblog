from django.urls import path,include
from . import views
app_name = "articles"
urlpatterns = [
    path ('',views.article_list,name= "list"),
    path ('<valslug>',views.article_detail , name= "detail"),
]

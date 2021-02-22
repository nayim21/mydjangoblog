from django.urls import path,include
from . import views
app_name = "articles"
urlpatterns = [
    path ('',views.article_list,name= "list"),
    path ('create' ,views.article_create,name= "create"),
    path ('<valslug>',views.article_detail , name= "detail"),
]

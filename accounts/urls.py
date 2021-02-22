from django.urls import path
from . import views
app_name = "accounts"
urlpatterns = [
    path('signup', views.signup_view , name= 'signup'),
    # path ('signup',views.signup , name="signup"),
    path ('login',views.login_view , name='login' ),
    path ('logout',views.logout_view , name='logout' ),

    # path ('',views.article_list,name= "list"),

]

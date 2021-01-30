from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name='accounts'

urlpatterns = [
    path('',views.indexView,name="home"),
    path('main/',views.mainView,name="main"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView, name="register_url"),
    #path('logout/'),
]
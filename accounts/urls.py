from django.urls import path,re_path
from . import views
from .views import  RegisterView, LoginView, LogoutView
app_name='start'
urlpatterns=[
	path("",views.index,name="index"),
	path("login/",LoginView.as_view(),name="login"),
	path("signup/",RegisterView.as_view(),name="signup"),
	path("logout/",LogoutView.as_view(),name="logout")
	] 
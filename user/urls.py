from django.urls import path
from . import views

app_name="user"

urlpatterns = [
    path("need_account/",views.need_account,name="need_account"),
    path("logout/",views.logout,name="logout"),
    path("register/",views.register,name="register"),
    path("login/",views.loginPage,name="login"),
    path("profile/",views.profile,name="profile"),
]

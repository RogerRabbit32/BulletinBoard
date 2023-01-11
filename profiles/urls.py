from django.urls import path, include
from django.contrib.auth.views import auth_login

from .views import signup_view, awaiting_confirmation, account_confirmation, logout_view

urlpatterns = [
    path('signup/', signup_view, name="signup"),
    path('confirmation/', account_confirmation, name="confirm"),
    path('login/', auth_login, name="login"),
    path('logout/', logout_view, name="logout"),
    path('/', include("django.contrib.auth.urls"))
]

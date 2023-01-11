from django.urls import path
from .views import logged_view, PostList, PostCreate

urlpatterns = [
    path('', PostList.as_view(), name="home"),
    path('new', PostCreate.as_view(), name='post_create'),
    path('logged/', logged_view)
]

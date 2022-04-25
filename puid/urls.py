from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='Puid Web'),
        # path('login_user', views.login_user, name="login"),
        path('about', views.about, name='puid result'),
]
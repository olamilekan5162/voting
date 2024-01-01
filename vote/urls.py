from django.urls import path
from . import views
from voting import urls

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('vote<str:pk>', views.vote, name='vote'),

]
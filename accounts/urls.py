from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('sing_up/', views.sing_up_views, name='sing_up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('sing_up/', views.sing_up_view, name='sing_up'),
]
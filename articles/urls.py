from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('',views.articles_list,name="List"),
    path('<slug>',views.articles_detail,name="Detail"),
]
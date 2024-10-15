from django.contrib import admin
from django.urls import path , include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#for ezafe shodn in urls hamon
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('contact/', views.contact),
    path('blog/', views.blog),
    path('', views.home),

    path('articles/', include('articles.urls')),
]
urlpatterns += staticfiles_urlpatterns()
#baraye ezafe shodn be list bala
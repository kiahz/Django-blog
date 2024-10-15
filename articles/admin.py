from django.contrib import admin
from . import models#ba in tag vasl mishe be admin

admin.site.register(models.Article)
# vasl kardan article dr model be safe admin

from django.contrib import admin

from articles.models import Article

# Register your models here.
admin.site.site_header = "News Editor Admin"
admin.site.register(Article)
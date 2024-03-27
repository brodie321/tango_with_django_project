from django.contrib import admin
from rango.models import Category, Page

admin.site.register(Category)



# Register your models here.
class PageAdminModel(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdminModel)

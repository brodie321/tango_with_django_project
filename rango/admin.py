from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
class PageAdminModel(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Page, PageAdminModel)
admin.site.register(Category, CategoryAdmin)

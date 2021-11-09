from django.contrib import admin
from .models import *



class ArticlesInline(admin.TabularInline):
    model = Article

class AdminArticles(admin.ModelAdmin):
    list_display = [field.name for field in Article._meta.fields]

    class Meta:
        model = Article

class AdminCategory(admin.ModelAdmin):
    list_display = [field.name for field in Categories._meta.fields]
    inlines = [ArticlesInline]
    class Meta:
        model = Categories

class AdminTasks(admin.ModelAdmin):
    list_display = [field.name for field in Task._meta.fields]

    class Meta:
        model = Task


admin.site.register(Article, AdminArticles)
admin.site.register(Task, AdminTasks)
admin.site.register(Categories, AdminCategory)
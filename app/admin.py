from django.contrib import admin
from .models import GetInTouch, Project

admin.site.register(GetInTouch)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'status')
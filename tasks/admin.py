from django.contrib import admin

from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display=["description"]

admin.site.register(Task, TaskAdmin)
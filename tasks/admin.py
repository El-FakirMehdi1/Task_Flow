from django.contrib import admin
from .models import Category,Task
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','color']
    search_fields = ['name']
    ordering = ['name']
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','category','priority','Completed','due_date']
    search_fields = ['title']
    list_filter = ['category','priority','Completed']
    list_editable = ['category','priority','Completed','due_date']
    ordering = ['-created_at']
    readonly_fields = ['created_at','updated_at']
    list_per_page = 20
    date_hierarchy = "created_at"


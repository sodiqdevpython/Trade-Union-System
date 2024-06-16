from django.contrib import admin
from .models import UnderAgeChildren, HandicappedDocsModel, RoleNoteModel, Job, Employee

@admin.register(UnderAgeChildren)
class UnderAgeChildrenAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'created_at', 'updated_at')
    search_fields = ('id',)
    date_hierarchy = 'created_at'
    list_per_page = 20

@admin.register(HandicappedDocsModel)
class HandicappedDocsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'type', 'created_at', 'updated_at')
    search_fields = ('id', 'type')
    list_filter = ('type',)
    date_hierarchy = 'created_at'
    list_per_page = 20

@admin.register(RoleNoteModel)
class RoleNoteModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'type', 'created_at', 'updated_at')
    search_fields = ('id', 'type')
    list_filter = ('type',)
    date_hierarchy = 'created_at'
    list_per_page = 20

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    list_per_page = 20

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'tel_number', 'id_card', 'born_in', 'employment_at', 'job', 'salary', 'score', 'allocated_funds', 'created_at', 'updated_at')
    search_fields = ('user__first_name', 'user__last_name', 'tel_number', 'id_card')
    list_filter = ('gender', 'job', 'born_in', 'employment_at', 'created_at', 'updated_at')
    date_hierarchy = 'employment_at'
    list_per_page = 20

    class Media:
        js = ('admin/js/vendor/jquery/jquery.js', 'admin/js/jquery.init.js', 'admin/js/actions.js')

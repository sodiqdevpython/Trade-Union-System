# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UnderAgeChildren, HandicappedDocsModel, RoleNoteModel, Job, UserExtraData

class UserAdmin(BaseUserAdmin):
    list_display = ('id_card', 'is_active', 'is_staff', 'is_verified', 'is_superuser', 'date_joined', 'last_joined')
    search_fields = ('id_card',)
    list_filter = ('is_active', 'is_staff', 'is_verified', 'is_superuser', 'date_joined', 'last_joined')
    list_per_page = 20
    date_hierarchy = 'date_joined'
    ordering = ('id_card',)
    fieldsets = (
        (None, {'fields': ('id_card', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_verified', 'is_superuser')}),
    )
    readonly_fields = ('date_joined', 'last_joined')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id_card', 'password1', 'password2', 'is_active', 'is_staff', 'is_verified', 'is_superuser')}
        ),
    )

class UnderAgeChildrenAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    list_per_page = 20
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')

class HandicappedDocsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'type', 'created_at', 'updated_at')
    list_filter = ('type', 'created_at', 'updated_at')
    list_per_page = 20
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')

class RoleNoteModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'type', 'created_at', 'updated_at')
    list_filter = ('type', 'created_at', 'updated_at')
    list_per_page = 20
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')

class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    list_per_page = 20
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')

class UserExtraDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'last_name', 'father_name', 'under_age_children_number', 'born_in', 'employment_at', 'salary', 'score', 'allocated_funds')
    search_fields = ('name', 'last_name', 'father_name')
    list_filter = ('born_in', 'employment_at', 'under_age_children_number', 'score', 'allocated_funds')
    list_per_page = 20
    date_hierarchy = 'born_in'
    readonly_fields = ('allocated_funds',)

admin.site.register(User, UserAdmin)
admin.site.register(UnderAgeChildren, UnderAgeChildrenAdmin)
admin.site.register(HandicappedDocsModel, HandicappedDocsModelAdmin)
admin.site.register(RoleNoteModel, RoleNoteModelAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(UserExtraData, UserExtraDataAdmin)

from .models import Organization, Event, Application, SpiritualRest, Accidents
from organization.models import Organization
from django.contrib import admin


# @admin.register(Organization)
# class OrganizationAdmin(admin.ModelAdmin):
#     list_display = ('title', 'phone_number')
#     search_fields = ('title', 'phone_number')
#     list_filter = ('title',)


# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'spend_money',
#                     'created_at', 'updated_at')
#     search_fields = ('title', 'author__first_name', 'author__last_name')
#     list_filter = ('author', 'created_at', 'updated_at')
#     date_hierarchy = 'created_at'


# @admin.register(Application)
# class ApplicationAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author_application',
#                     'status_application', 'created_at', 'updated_at')
#     search_fields = ('title', 'author_application__first_name',
#                      'author_application__last_name')
#     list_filter = ('status_application', 'created_at', 'updated_at')
#     date_hierarchy = 'created_at'


# @admin.register(Application)
# class ApplicationAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author_application',
#                     'status_application', 'created_at', 'updated_at', )
#     search_fields = ('title', 'author_application__first_name',
#                      'author_application__last_name')
#     list_filter = ('status_application', 'created_at', 'updated_at')
#     date_hierarchy = 'created_at'


# @admin.register(SpiritualRest)
# class SpiritualRestAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created_at', 'updated_at')
#     search_fields = ('name', 'who_are_invited__first_name',
#                      'who_are_invited__last_name')
#     list_filter = ('created_at', 'updated_at')
#     filter_horizontal = ('who_are_invited',)
#     date_hierarchy = 'created_at'


# @admin.register(Accidents)
# class AccidentsAdmin(admin.ModelAdmin):
#     list_display = ('who', 'spend_money', 'created_at', 'updated_at')
#     search_fields = ('who__first_name', 'who__last_name')
#     list_filter = ('who', 'created_at', 'updated_at')
#     date_hierarchy = 'created_at'

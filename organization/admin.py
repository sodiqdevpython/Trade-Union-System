from django.contrib import admin
from .models import Organization, Event, Application, SpiritualRest, Accidents, IDCards, Money

admin.site.register(IDCards)

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone_number', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'phone_number', 'description')
    list_filter = ('created_at', 'updated_at')
    list_per_page = 20
    date_hierarchy = 'created_at'

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'spend_money', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')
    list_per_page = 20
    date_hierarchy = 'created_at'

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_application', 'status_application', 'created_at', 'updated_at')
    search_fields = ('title', 'body',)
    list_filter = ('status_application', 'created_at', 'updated_at')
    list_per_page = 20
    date_hierarchy = 'created_at'

class SpiritualRestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')
    list_per_page = 20
    date_hierarchy = 'created_at'

class AccidentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'spend_money', 'more_info', 'created_at', 'updated_at')
    search_fields = ('more_info',)
    list_filter = ('created_at', 'updated_at')
    list_per_page = 20
    date_hierarchy = 'created_at'

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(SpiritualRest, SpiritualRestAdmin)
admin.site.register(Accidents, AccidentsAdmin)
admin.site.register(Money)
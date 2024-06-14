from django.contrib import admin
from .models import IdCards, ApplicationStatusModel, Organization, Event, Application, SpiritualRest, Accidents

@admin.register(IdCards)
class IdCardsAdmin(admin.ModelAdmin):
    list_display = ('card_id', 'is_active')
    search_fields = ('card_id',)
    list_filter = ('is_active',)

@admin.register(ApplicationStatusModel)
class ApplicationStatusModelAdmin(admin.ModelAdmin):
    list_display = ('status', 'who_rejected')
    search_fields = ('status', 'who_rejected__first_name', 'who_rejected__last_name')
    list_filter = ('status',)
    filter_horizontal = ('who_are_viewed',)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel_number')
    search_fields = ('name', 'tel_number')
    list_filter = ('name',)
    filter_horizontal = ('staffs', 'id_cards')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'spend_money', 'created_at', 'updated_at')
    search_fields = ('name', 'author__first_name', 'author__last_name')
    list_filter = ('author', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_application', 'status_application', 'created_at', 'updated_at')
    search_fields = ('title', 'author_application__first_name', 'author_application__last_name')
    list_filter = ('status_application', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'

@admin.register(SpiritualRest)
class SpiritualRestAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'who_are_invited__first_name', 'who_are_invited__last_name')
    list_filter = ('created_at', 'updated_at')
    filter_horizontal = ('who_are_invited',)
    date_hierarchy = 'created_at'

@admin.register(Accidents)
class AccidentsAdmin(admin.ModelAdmin):
    list_display = ('who', 'spend_money', 'created_at', 'updated_at')
    search_fields = ('who__first_name', 'who__last_name')
    list_filter = ('who', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'

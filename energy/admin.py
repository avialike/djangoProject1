from django.contrib import admin
from energy.models import Client, Service, Data_transfer, News
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['user_service', 'service_name', 'site', 'personal_account']
    list_filter = ['user_service', 'service_name']
    pass

class DataAdmin(admin.ModelAdmin):
    list_display = ['user_transfer', 'date', 'value']
    pass

class serviceInline(admin.TabularInline):
    model = Service

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_service_count']
    inlines = [
        serviceInline
    ]

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'date_posted']

admin.site.register(Client, ClientAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Data_transfer, DataAdmin)
admin.site.register(News, NewsAdmin)

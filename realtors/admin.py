from django.contrib import admin
from . models import Realtor
# Register your models here.
class realtorAdmin(admin.ModelAdmin):
    list_display=('id','name','email','hire_date')
    list_display_links=('name',)
    search_fields=('name',)
    list_per_page=25

admin.site.register(Realtor, realtorAdmin)

from django.contrib import admin
from .models import Quote

# Register your models here.
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'contact_name', 'brazed', 'date')
    list_filter = ('brazed',)
    search_fields = ('business_name', 'contact_name')

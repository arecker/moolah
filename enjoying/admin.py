from django.contrib import admin

from models import Purchase

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('description', 'timestamp', 'amount', 'user')


admin.site.register(Purchase, PurchaseAdmin)

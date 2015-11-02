from django.contrib import admin
from models import Rate, Transaction


class RateAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount_per_day', 'amount', 'days')


class TranactionAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'timestamp')


admin.site.register(Rate, RateAdmin)
admin.site.register(Transaction, TranactionAdmin)

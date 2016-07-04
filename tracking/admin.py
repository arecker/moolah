from django.contrib import admin

from models import (Rate, Allowance, Transaction)


class RateAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount_per_day', 'amount', 'days')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'allowance', 'timestamp')
    list_filter = ('allowance',)


admin.site.register(Rate, RateAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Allowance)

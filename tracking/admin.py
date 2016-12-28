from django.contrib import admin

from models import (Rate, Allowance, Transaction)


class RateAdmin(admin.ModelAdmin):
    list_display = ('description', 'active', 'amount_per_day', 'amount', 'days')
    list_filter = ('active', )


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'allowance', 'timestamp')
    list_filter = ('allowance',)


admin.site.register(Rate, RateAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Allowance)

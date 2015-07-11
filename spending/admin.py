from django.contrib import admin
from .models import (
    Period,
    Transaction,
    Budget
)


class TransactionInline(admin.StackedInline):
    model = Transaction
    extra = 0


class PeriodAdmin(admin.ModelAdmin):
    inlines = (TransactionInline, )
    list_filter = ('reoccuring', )


admin.site.register(Period, PeriodAdmin)
admin.site.register(Budget)

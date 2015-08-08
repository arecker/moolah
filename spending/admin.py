from django.contrib import admin
from .models import (
    Period,
    Transaction,
    Budget
)


class PeriodAdmin(admin.ModelAdmin):
    list_filter = ('reoccuring', )


admin.site.register(Period, PeriodAdmin)
admin.site.register(Budget)
admin.site.register(Transaction)

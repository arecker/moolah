from django.contrib import admin

from models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('description', 'timestamp', 'amount', 'user')


admin.site.register(Transaction, TransactionAdmin)

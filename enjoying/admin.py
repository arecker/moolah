from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from enjoying.models import Allowance, Purchase

class AllowanceAdmin(admin.StackedInline):
    model = Allowance


class UserAdmin(UserAdmin):
    inlines = (AllowanceAdmin, )


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('description', 'timestamp', 'amount', 'allowance')
    list_filter = ('allowance', )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Purchase, PurchaseAdmin)

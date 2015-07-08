from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import Account


class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (AccountInline, )


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)

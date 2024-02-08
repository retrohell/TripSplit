from django.contrib import admin
from .models import Guest, Group, UserGroup, Payment, Expense, ExpenseParticipant

# Register your models here.

# User
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

admin.site.register(Guest, UserAdmin)

# Group
admin.site.register(Group)

# UserGroup
class UserGroupAdmin(admin.ModelAdmin):
    def guest_id(self, obj):
        return obj.Guest.username
    def group_id(self, obj):
        return obj.group.name
    list_display = ('guest_id', 'group_id')

admin.site.register(UserGroup, UserGroupAdmin)

# Payment
class PaymentAdmin(admin.ModelAdmin):
    def payer_id(self, obj):
        return obj.payer.name
    def receiver_id(self, obj):
        return obj.receiver.name
    list_display = ('payer_id', 'receiver_id', 'amount', 'created_at')

admin.site.register(Payment, PaymentAdmin)

# Expenses
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('payer', 'amount', 'description', 'created_at', 'updated_at')

admin.site.register(Expense, ExpenseAdmin)

# ExpenseParticipant
class ExpenseParticipantAdmin(admin.ModelAdmin):
    list_display = ('expense_id', 'participant_id')

admin.site.register(ExpenseParticipant, ExpenseParticipantAdmin)




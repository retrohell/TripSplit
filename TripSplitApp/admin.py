from django.contrib import admin
from .models import User, Group, UserGroup, Payment, Expense, ExpenseParticipant

admin.site.register(User)
admin.site.register(Group)
admin.site.register(UserGroup)
admin.site.register(Payment)
admin.site.register(Expense)
admin.site.register(ExpenseParticipant)


# Register your models here.

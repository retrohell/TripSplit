from django.db import models
from .m_expense import Expense
from .m_guest import Guest

class ExpenseParticipant(models.Model):
    expense_id = models.ForeignKey(Expense, on_delete=models.RESTRICT, related_name='expense')
    participant_id = models.ForeignKey(Guest, on_delete=models.RESTRICT, related_name='participant')


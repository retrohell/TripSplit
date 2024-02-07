from django.db import models
from .m_user import Guest
import uuid

class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payer = models.ForeignKey(Guest, on_delete=models.RESTRICT, related_name='payer_expense')
    amount = models.FloatField()
    description = models.CharField(max_length=100)
    created_at = models.DateField()
    updated_at = models.DateField()
from django.db import models
from .m_user import Guest
import uuid
   
class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payer_id = models.ForeignKey(Guest, on_delete=models.RESTRICT, related_name='payer_payment')
    receiver_id = models.ForeignKey(Guest, on_delete=models.RESTRICT, related_name='receiver')
    amount = models.FloatField()
    created_at = models.DateField()
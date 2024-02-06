from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username + " - " + self.email 
    
class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    
class UserGroup(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='user')
    group_id = models.ForeignKey(Group, on_delete=models.RESTRICT, related_name='group')
    
class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payer_id = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='payer_payment')
    receiver_id = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='receiver')
    amount = models.FloatField()
    created_at = models.DateField()

class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payer = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='payer_expense')
    amount = models.FloatField()
    description = models.CharField(max_length=100)
    created_at = models.DateField()
    updated_at = models.DateField()

class ExpenseParticipant(models.Model):
    expense_id = models.ForeignKey(Expense, on_delete=models.RESTRICT, related_name='expense')
    participant_id = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='participant')


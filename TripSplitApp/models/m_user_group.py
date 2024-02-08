from django.db import models
from .m_guest import Guest
from .m_group import Group
   
class UserGroup(models.Model):
    guest_id = models.ForeignKey(Guest, on_delete=models.RESTRICT, related_name='guest')
    group_id = models.ForeignKey(Group, on_delete=models.RESTRICT, related_name='group')
from django.db import models
from django.contrib.auth.models import User
from . import utils




# Create your models here.
class Website(models.Model):
    site = models.CharField(max_length = 200, blank=False, null=False)
    username = models.CharField(max_length=200, blank=False,null=False)
    password=models.CharField(max_length=200, blank=False,null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.site + ' ' + self.username
    
    @property
    def get_password(self):
        return utils.decrypt(self.password)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.password = utils.encrypt(self.password)
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

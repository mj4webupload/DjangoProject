from django.db import models

# Create your models here.
class Role(models.Model):
    Role = models.CharField(max_length=25)
    
    class Meta:
        db_table = 'shop_login'
from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    first_nume = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number_of_login = models.IntegerField()

    class Meta:
        db_table = "usersmodels"
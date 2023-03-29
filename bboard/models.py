from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.models import AbstractUser

from django.db import models

class Students(models.Model):
    name = models.CharField('Имя', max_length=50)
    lastname = models.CharField('Фамилия', max_length=50)
    middlename = models.CharField('Отчество', max_length=50)
    birthday = models.DateField('День рождения')
    diploma_title = models.CharField('Тема дипломного проекта', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Student'


# secretaries_group = Group.objects.create(name='secretaries')
# commission_group = Group.objects.create(name='commission')
#
# class CustomUser(AbstractUser):
#     is_secretary = models.BooleanField(default=False)
#     is_commission = models.BooleanField(default=False)
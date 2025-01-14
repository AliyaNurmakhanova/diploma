from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.models import AbstractUser

from django.db import models

class Students(models.Model):
    img = models.ImageField(upload_to='images')
    name = models.CharField('Имя', max_length=50)
    lastname = models.CharField('Фамилия', max_length=50)
    middlename = models.CharField('Отчество', max_length=50)
    birthday = models.DateField('День рождения')
    diploma_title = models.CharField('Тема дипломного проекта', max_length=100)
    iin = models.CharField('ИИН', max_length=100, default=' ')
    name_eng = models.CharField('Имя на английском', max_length=100, default=' ')
    lastname_eng = models.CharField('Фамилия на английском', max_length=100, default=' ')
    middlename_eng = models.CharField('Отчество на английском', max_length=100, default=' ')
    id_card = models.CharField('№ удостоверения личности/паспорта', max_length=100, default=' ')
    speciality = models.CharField('Специальность', max_length=100, default=' ')
    prez_diploma = models.FileField('Презентация', upload_to='uploads/')
    recen_diploma = models.FileField('Рецензия', upload_to='uploads/')
    feedback_diploma = models.FileField('Отзыв руководителя', upload_to='uploads/')
    antiplagiat = models.FileField('Антиплагиат', upload_to='uploads/')

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
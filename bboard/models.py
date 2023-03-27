from django.db import models

class Students(models.Model):
    name_kz = models.CharField('Имя', max_length=50)
    lastname_kz = models.CharField('Фамилия', max_length=50)
    middlename_kz = models.CharField('Отчество', max_length=50)
    birthday = models.DateField('День рождения')
    diploma_title = models.CharField('Тема дипломного проекта', max_length=100)
    stud_id = models.IntegerField('ИИН', max_length=12)

    def __str__(self):
        return self.name_kz

    class Meta:
        verbose_name = 'Student'
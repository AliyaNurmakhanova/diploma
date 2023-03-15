from django.db import models

class Students(models.Model):
    name = models.CharField('Имя', max_length=50)
    lastname = models.CharField('Фамилия', max_length=50)
    middlename = models.CharField('Отчество', max_length=50)
    birthday = models.DateField('День рождения')
    stud_id = models.IntegerField('ИИН', max_length=12)
    diploma_title = models.CharField('Тема дипломного проекта', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студенты'
from django.db import models

class Students(models.Model):
    img = models.ImageField(upload_to='images')
    name = models.CharField('Имя', max_length=50)
    lastname = models.CharField('Фамилия', max_length=50)
    middlename = models.CharField('Отчество', max_length=50)
    birthday = models.DateField('День рождения')
    diploma_title = models.CharField('Тема дипломного проекта', max_length=100)
    iin = models.CharField('ИИН', max_length=100, default='ИИН')
    # name_eng = models.CharField('Имя на английском', max_length=100, default='Имя')
    # lastname_eng = models.CharField('Фамилия на английском', max_length=100, default='Фамилия')
    # middlename_eng = models.CharField('Отчество на английском', max_length=100, default='Отчество')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Student'
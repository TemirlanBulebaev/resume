from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)# Заголовок
    description = models.CharField(max_length=250) # Описание
    image = models.ImageField(upload_to='portfolio/images/')# Изображения
    url = models.URLField(blank=True)# Переход по клику






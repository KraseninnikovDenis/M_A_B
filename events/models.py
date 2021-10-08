from django.db import models

class EventsDB  (models.Model):
    event_image= models.ImageField(upload_to='image_event/', verbose_name='картинка')
    event_text=models.CharField(max_length=100, verbose_name= 'описание')

    class Meta:
        verbose_name_plural='Ивенты'
        verbose_name='Ивент'
from django.db import models

class EventsDB  (models.Model):
    event_image= models.ImageField(upload_to='image_event/', verbose_name='картинка')
    event_text=models.CharField(max_length=100, verbose_name= 'описание')

    def __str__ (self):
        return self.event_text

    class Meta:
        verbose_name_plural='Ивенты'
        verbose_name='Ивент'
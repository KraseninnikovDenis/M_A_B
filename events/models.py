from django.db import models

class EventsDB  (models.Model):
    event_image= models.ImageField(upload_to='image_event/')
    event_text=models.CharField(max_length=100)

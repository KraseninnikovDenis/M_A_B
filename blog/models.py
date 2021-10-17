from django.db import models

# Create your models here.
class Post (models.Model):
    title=models.CharField(max_length=50, verbose_name='заголовок')
    date=models.DateField(auto_now_add=True, verbose_name='дата')
    text=models.TextField(verbose_name='текст поста')
    image=models.ImageField(upload_to='image_event/', verbose_name='картинка')

    def brief_text(self):
        return self.text[:30] + ' ...'
    
    class Meta:
        verbose_name_plural='посты'
        verbose_name='Пост'

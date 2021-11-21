from django.db import models

class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    intro = models.CharField('intro', max_length=250)
    full_text = models.TextField('article')
    date = models.DateTimeField('public')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/article/{self.id}'
    class Meta:
        verbose_name= 'article'
        verbose_name_plural = 'articles'
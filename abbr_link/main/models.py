from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Link(models.Model):
    link = models.URLField("Ссылка", max_length=150)
    min_link = models.CharField("Короткая ссылка", max_length=100, unique=True)
    author = models.ForeignKey(User, verbose_name="Автор", blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.min_link
    
    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"
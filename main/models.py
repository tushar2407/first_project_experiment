from django.db import models

# Create your models here.
class Question(models.Model):
    title=models.CharField(max_length=256)
    body=models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="A Question"
        verbose_name_plural="The Questions"
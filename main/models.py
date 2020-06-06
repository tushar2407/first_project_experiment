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

class Book(models.Model):
    title=models.CharField(max_length=256)
    author=models.CharField(max_length=256)
    pdf=models.FileField(upload_to='books/pdf/')
    cover=models.ImageField(upload_to="books/covers/", null=True, blank=True)
    def __str__(self):
        return self.name
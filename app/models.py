from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=300)
    messages = models.TextField()

    class Meta:
        verbose_name = ('Contact')
        verbose_name_plural = ('Contacts')

    def __str__(self):
        return self.full_name


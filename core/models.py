from django.db import models


class People(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()

    class Meta:
        verbose_name="Pessoa"
        verbose_name_plural="Pessoas"
        ordering=['name']
    
    def __str__(self):
        return self.name
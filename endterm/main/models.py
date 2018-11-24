from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Person(models.Model):
    id = models.IntegerField(max_length=20)
    FullName = models.CharField(max_length=100)
    #Date = models.DateField('date of getting')
    Gender = models.IntegerField(max_length=1)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __str__(self):
        return self.name

class Category:
    id = models.IntegerField(max_length=20)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_plural_name = 'Categories'

    def __str__(self):
        return self.name


class Achievements(models.Model):
    id = models.IntegerField(max_length=20)
    Personid= models.ForeignKey(Person, on_delete=models.CASCADE)
    Categoryid = models.ForeignKey(Category, on_delete=models.CASCADE)
    Date = models.DateTimeFieldField('date of getting ')
    Title = models.CharField(max_length=100)

    def __str__(self):
        return self.id


def to_json(self):
    return {
            'id': self.id,
            'Perso': self.name,
            'user': self.created_by.username if self.created_by else None
        }
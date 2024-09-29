from django.db import models

# Create your models here.
class Type(models.Model) :
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_types():
        return Type.objects.all()

    def __str__(self):
        return self.name


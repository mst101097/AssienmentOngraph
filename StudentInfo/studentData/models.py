from django.db import models

# Create your models here.
class StudentModel(models.Model):
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length = 30)
    lastName = models.CharField(max_length = 30)
    score = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.firstName

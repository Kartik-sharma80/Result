from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.CharField(max_length=20, null=True)
    year = models.CharField(null=True, max_length=20)
    file = models.FileField(upload_to="", null=False, blank=False)

    def __str__(self):
        return self.roll_no
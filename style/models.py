from django.db import models

# Create your models here.


class Style(models.Model):
    module_id = models.CharField(max_length = 300, blank = True, null = True)
    title = models.CharField(max_length = 50)
    instructor = models.CharField(max_length = 20)
    module_course = models.CharField(max_length= 30)
    academic_year = models.CharField(max_length = 10)
    type = models.CharField(max_length= 50)
    description = models.CharField(max_length= 200)

    def __str__(self):
        return self.title
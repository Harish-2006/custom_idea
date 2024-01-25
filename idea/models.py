from django.db import models

class name(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class email(models.Model):
    mail = models.EmailField(null = True, blank = True)

    def __str__(self):
        return self.mail

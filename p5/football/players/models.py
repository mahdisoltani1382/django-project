from django.db import models

class teams(models.Model):
    team = models.CharField(max_length=128)
    post = models.CharField(max_length=128)
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

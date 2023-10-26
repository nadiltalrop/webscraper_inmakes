from django.db import models


class Link(models.Model):
    address = models.CharField(max_length=500,blank=True,null=True)
    string_name = models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return self.string_name
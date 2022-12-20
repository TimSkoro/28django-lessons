from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='event')


class OverFirst(models.Model):
    field_0 = models.CharField(max_length=200)
    field_1 = models.IntegerField(default=10)
    field_2 = models.FloatField(null=True)
    field_3 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.field_0} - {self.field_3}"



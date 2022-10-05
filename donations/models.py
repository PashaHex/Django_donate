from django.db import models

class Office(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    occupied = models.IntegerField()

    def __str__(self):
        return f'{self.name}({self.capacity}, {self.occupied})'

class Item(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    state = models.BooleanField(
        choices=((0, 'Available'), (1, 'Booked')), default=0
    )
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True)
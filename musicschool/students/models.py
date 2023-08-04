from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    age = models.IntegerField()
    course = models.IntegerField()
    instrument_choices = (('g', 'guitar'), ('p', 'piano'), ('r', 'recorder'), ('t', 'trumpet'))
    instrument = models.CharField(max_length=60, choices=instrument_choices)
    performance = models.IntegerField()
    paid_for_studies = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.instrument} - {self.performance}'
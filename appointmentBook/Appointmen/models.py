from django.db import models

specialist_doctor = [
    ('neurologist', 'Neurologist'),
    ('dentist', 'Dentist'),
    ('gyneacologist', 'Gynecologist'),
    ('cardiologist', 'Cardiologist'),
]

class Doctor_Info(models.Model):
    name = models.CharField(max_length=100)
    specialist = models.CharField(max_length=100, choices=specialist_doctor)
    available_from = models.TimeField()
    available_to = models.TimeField()

    def __str__(self):
        return f'Dr. {self.name} ({self.specialist})'

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    doctor = models.ForeignKey(Doctor_Info, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    symptoms = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.patient_name} - {self.symptoms} on {self.date}"

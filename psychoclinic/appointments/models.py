from django.db import models
from users.models import Doctor, Patient

# Create your models here.
class Appointment(models.Model):
    
    status_choices = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('rescheduled', 'Rescheduled'),
        ('no-show', 'No-show'),
    ]
    
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, db_column='doctor')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient')
    date_appointment = models.DateTimeField()
    status = models.CharField(max_length=255, choices=status_choices)

    def __str__(self):
        return f'{self.date_appointment.strftime("%d/%m/%Y %H:%M")} - doctor:{self.doctor} - patient:{self.patient}'

    class Meta:
        db_table = 'appointment'
        managed = True
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
from django.db import models

# Create your models here.


#MEDICO
class Medico(models.Model):
    nombre_m = models.CharField(max_length=100)
    apellido_m = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_m

    class Meta:
        verbose_name_plural = ("Medico")

#OrdenLaboratorio
class OrdenLaboratorio(models.Model):
    medico = models.ForeignKey(Medico, null=True, on_delete=models.CASCADE)
    fecha= models.DateField()
    examen = models.CharField(max_length=100)

    def __str__(self):
        return self.examen

    class Meta:
        verbose_name_plural = ("OrdenLaboratorio")
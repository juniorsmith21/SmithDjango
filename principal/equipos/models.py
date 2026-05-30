from django.db import models

# Create your models here.
class Equipo(models.Model):

    TIPO_CHOICES=[
        ('electrico', 'Electrico'),
        ('mecanico', 'Mecanico'),
        ('hidraulico', 'Hidraulico'),
        ('neumatico', 'Neumatico'),
        ('electronico', 'Electronico'),


    ]

    nombre                  =models.CharField(max_length=150)
    codigo                  =models.CharField(max_length=50, unique=True)
    tipo                    =models.CharField(max_length=50, choices=TIPO_CHOICES)
    descripcion             =models.TextField(blank=True)
    ubicacion               =models.CharField(max_length=200)
    fecha_adquisicion    =models.DateField()
    activo                  =models.BooleanField(default=True)


    def __str__(self):
        return f'[{self.codigo}] {self.nombre}'
    class Meta:
        ordering=['nombre']
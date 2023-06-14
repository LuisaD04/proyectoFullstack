from django.db import models

# Create your models here.
class Voluntarios(models.Model):
    cedulaVoluntario = models.IntegerField(primary_key=True)
    nombreVoluntario = models.CharField(max_length=100)
    apellidoVoluntario = models.CharField(max_length=100)
    edadVoluntario = models.IntegerField()
    correoVoluntario = models.EmailField(max_length=100)
    ciudadVoluntario = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.cedulaVoluntario}'
    
class Delegados(models.Model):
    idDelegado = models.IntegerField(primary_key=True)
    nombreDelegado = models.CharField(max_length=100)
    apellidoDelegado = models.CharField(max_length=100)
    cedulaDelegado = models.IntegerField()
    edadDelegado = models.IntegerField()
    correoDelegado = models.CharField(max_length=100)
    ciudadDelegado = models.CharField(max_length=100)
    celularDelegado = models.IntegerField()

    def __str__(self):
        return f'{self.idDelegado}'
class Proyectos(models.Model):
    idProyecto = models.BigAutoField(primary_key=True)
    nombreProyecto = models.CharField(max_length=200)
    descripcionProyecto = models.TextField(max_length=500)
    def __str__(self):
        return f'{self.idProyecto}'

class Categorias(models.Model):
    idCategoria = models.BigAutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=200)
    nombreContenido = models.TextField(max_length=500)
    descripciónContenido = models.TextField(max_length=500)
    imagenContenido = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'{self.idCategoria}'    

class Seguimiento(models.Model):
    idRegistro = models.BigAutoField(primary_key=True)
    cedulaVoluntarioSeguimiento = models.ForeignKey(Voluntarios , on_delete=models.CASCADE , null=True)
    cedulaDelegadoSeguimiento = models.ForeignKey(Delegados , on_delete=models.CASCADE , null=True)
    idProyectoSeguimiento = models.ForeignKey(Proyectos , on_delete=models.CASCADE , null=True)
    faseSeguimiento = models.IntegerField()
    avanceMeta = models.IntegerField()
    def __str__(self):
        return f'{self.idRegistro}'
    
class ZonasRecuperadas(models.Model):
    idZona = models.BigAutoField(primary_key=True)
    idCategoriaZona = models.ForeignKey(Categorias , on_delete=models.CASCADE , null=True)
    cedulaDelegadoSeguimiento = models.ForeignKey(Delegados , on_delete=models.CASCADE , null=True)
    cedulaVoluntarioSeguimiento = models.ForeignKey(Voluntarios , on_delete=models.CASCADE , null=True)
    nombreZona = models.CharField(max_length=200)
    descripcionZona = models.TextField(max_length=500)
    imagenZona = models.ImageField(upload_to='images/', blank=True, null=True)
    direccionZona = models.TextField(max_length=500)
    def __str__(self):
        return f'{self.idZona}'
    


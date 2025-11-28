from django.db import models
from datetime import date
from cloudinary.models import CloudinaryField
      
class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, verbose_name="Titulo")
    content = models.TextField(max_length=4000, null=False, blank=False, verbose_name="Contenido")
    date = models.DateField(default=date.today, verbose_name="Fecha de creacion")
    status = models.BooleanField(default=True, verbose_name="Estado")
    image = CloudinaryField('Imagen', folder="post", blank=False, null=False )
    slug = models.SlugField(unique=True,)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoria")
    tag = models.ManyToManyField(Tag, blank=True, verbose_name="Etiquetas")
    
    
    def __str__(self):
        return self.title
    
    
    
    
    
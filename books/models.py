from django.db import models

# Añadimos la seccion Category con los valores que habra en el campo.
class Category(models.Model):
    name = models.CharField(max_length=250)
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name

# Añadimos la seccion Book con los valores que habran en los campos.
class Book(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'
    CHOICES_STATUS = [
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft'),
    ]

    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)  
    author = models.CharField(max_length=250)  
    image = models.CharField(max_length=2000)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
from django.db import models

# New seccion of the code added (To get All URL Generated).
class Category(models.Model):
    title = models.CharField(max_length=250)
   
class Book(models.Model):

    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = {
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    }

    category = models.ForeignKey(Category, related_name='Book', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)  
    author = models.CharField(max_length=250)  
    image = models.CharField(max_length=2000)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

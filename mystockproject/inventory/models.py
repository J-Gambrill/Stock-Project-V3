from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Stock(models.Model): # Stock is the name of the model
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=75)
   
    description = models.TextField(max_length=500, blank=True, null=True) 
    
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=0  
    )
    
    IMPORTANCE_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    importance = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default='Low')

    STATUS_CHOICES = [
        ('Ordered', 'Ordered'),
        ('Denied', 'Denied'),
        ('Pending', 'Pending'),
    ]
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='Pending')

    
    createdAt = models.DateTimeField(auto_now_add=True)

    banner = models.ImageField(default='fallback.png',null=True, blank=True)  # Pillow installed first using terminal

    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, default=None) # this means should the user be deleted so will their posts

    slug = models.SlugField(unique=True, blank=True)
    #the code below will generate a unique slug so that the user does not have to input one 
    def save(self, *args, **kwargs):
        if not self.slug:  # Generate a slug only if it doesn't exist
            counter = 1
            original_slug = slugify(self.name)  # Define original_slug here
            self.slug = original_slug
            while Stock.objects.filter(slug=self.slug).exists():  # Check for duplicates
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
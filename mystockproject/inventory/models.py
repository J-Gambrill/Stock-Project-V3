from django.db import models

# Create your models here.

class Stock(models.Model): # Stock is the name of the model
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=75)
   
    description = models.TextField(max_length=500) 
    
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
    
    image = models.URLField(max_length=300, blank=True, null=True)

    banner = models.ImageField(default='fallback.png', blank=True)  # Pillow installed first using terminal

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
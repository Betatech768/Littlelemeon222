from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField( max_length=1000)
    # image = models.ImageField(upload_to= 'images/', default='static/default.jpg')
    
    def __str__(self):
        return self.name

class Menu (models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default='name')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/', default='static/default.jpg')
    
    def __str__(self):
        return self.name
    
    
    
class Take( models.Model):
    
    full_name = models.CharField(max_length=200)
    order = models.ForeignKey(Menu, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    city = models.CharField(max_length=100)
    timestamp = models.TimeField(auto_now_add=True )
    updated = models.DateTimeField(auto_now=True)
    
    class Meta: 
        ordering = ['-timestamp', '-updated']
    
    
    def __str__(self):
        return self.full_name + ' ' + str(self.order)  
    
    
class Booking (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    guest_number = models.IntegerField()
    comment = models.TextField(max_length=1000, null= True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta: 
        ordering = ['-created', 'updated']
    
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

class Contact(models.Model):
    Email = models.EmailField()
    Message = models.TextField(max_length= 5000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta: 
        ordering = ['-created', 'updated']
    
    def __str__(self):
        return self.Email    

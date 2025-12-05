from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=50,default="unknown")
    
    def __str__(self):
        return f"{self.name} ({self.age})"
    
class Course(models.Model): 
    course=models.CharField(max_length=100)
    duration=models.IntegerField()
    fees=models.IntegerField() 
    trainer = models.CharField(max_length=100,default="Trainer")
    description = models.TextField(default="No description available")
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.course
    

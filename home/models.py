
from django.db import models

# Create your models here.

class CV(models.Model):
    name=models.CharField(max_length=50)
    filepath=models.FileField(upload_to='cv/')


    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    title=models.CharField(max_length=200)
    start_time=models.DateField()
    end_time=models.DateField(blank=True,null=True)
    present_work=models.CharField(max_length=50,blank=True,default='Present')
    image=models.ImageField()
    description=models.TextField()

    def __str__(self):
        # return '{} --- {}'.format(self.title,self.description)
        return self.title

class BasicInfo(models.Model):
    
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=14)
    address=models.CharField(max_length=100)
    language=models.TextField(default='English, Bangla')
    
    def __str__(self):
        return '{} --- {}---{}'.format(self.age,self.email,self.phone)

class Certificate(models.Model):
    title=models.CharField(max_length=100)
    c_image=models.ImageField(upload_to='certificate_image/')
    description=models.TextField(blank=True)

    def __str__(self):
        return self.title



# Skills
class Skill(models.Model):
    choice=(
        ('Personal Skil','Personal Skil'),
        ('Hard Skil','Hard Skil'),
        
    )
    category=models.CharField(max_length=100,choices=choice)
    title=models.CharField(max_length=100)
    parcent=models.IntegerField()

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class MyProject(models.Model):

    choice=(
        ('Data Analysis','Data Analysis'),
        ('Machine Learning','Machine Learning'),
        ('Deep Learning','Deep Learning'),
        ('Web Development','Web Development'),
        
    )

    project_id=models.AutoField
    project_name=models.CharField(max_length=100)
    project_catagory=models.CharField(max_length=100,choices=choice)
    project_description=models.TextField()
    project_url=models.URLField()
    project_pic=models.ImageField(upload_to='project_img',blank=True,)


    def __str__(self):
        return self.project_name



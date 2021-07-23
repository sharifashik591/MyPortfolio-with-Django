from django.shortcuts import render
from project.models import MyProject
# Create your views here.
def project_detail(request):
    obj=MyProject.objects.all()

    context={
       'object':obj
    }
    return render(request,'home/project.html',context=context)

def Data_Analysis(request):
   obj=MyProject.objects.filter(project_catagory='Data Analysis')
   context={
       'object':obj
    }
   return render(request,'project/data_analysis.html',context=context)

def MachineLearning(request):
   obj=MyProject.objects.filter(project_catagory='Machine Learning')
   context={
       'object':obj
    }
   return render(request,'project/ml.html',context=context)

def DeepLearning(request):
   obj=MyProject.objects.filter(project_catagory='Deep Learning')
   context={
       'object':obj
    }
   return render(request,'project/deep_learning.html',context=context)


def Webdevelopment(request):
   obj=MyProject.objects.filter(project_catagory='Web Development')
   context={
       'object':obj
    }
   return render(request,'project/web_development.html',context=context)
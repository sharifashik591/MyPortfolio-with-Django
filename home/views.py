from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import WorkExperience,CV,BasicInfo,Certificate
# Create your views here.
def Home(request):

    obj=CV.objects.all()
    wor_exp=WorkExperience.objects.all()
    c_info=Certificate.objects.all()
    basic_info=BasicInfo.objects.last
    skill_obj=Skill.objects.filter(category="Hard Skil")
    personal_obj=Skill.objects.filter(category="Personal Skil")

    context={
        'cv':obj,
        'wor_exp':wor_exp,
        'basic_info':basic_info,
        'c_info': c_info,
        'skill_obj':skill_obj,
        'personal_obj':personal_obj,
    }

    return render(request,'home/home.html',context=context)

def CertificateInfo(request):
    c_info=Certificate.objects.all()
    contexts={'c_info':c_info}
    return render(request,'home/certificate_slide.html',context=contexts)

def About(request):
    wor_exp=WorkExperience.objects.all()
    c_info=Certificate.objects.all()
    basic_info=BasicInfo.objects.last
    

    context={
        'wor_exp':wor_exp,
        'basic_info':basic_info,
        'c_info': c_info,
    }
    return render(request,'home/about.html',context=context)

# Skill
from .models import Skill
def Skills(request):

    skill_obj=Skill.objects.filter(category="Hard Skil")
    personal_obj=Skill.objects.filter(category="Personal Skil")
    contexts={'skill_obj':skill_obj,
                'personal_obj':personal_obj,
                }
    return render(request,'home/skills.html',context=contexts)

def Work_experience(request):
    return render(request,'home/work_experience.html')


def Education(request):
    return render(request,'home/education.html')


def Contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # send_mail(
        #     'Test',
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [email],
        #     fail_silently=False,
        # )
        send_mail(
            'Test',
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        context={
            'user_name':name,

        }
        return render(request, 'home/contact.html',context=context)

    return render(request,'home/contact.html')



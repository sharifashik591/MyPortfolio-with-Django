from django.contrib import admin

from home.models import CV,WorkExperience,BasicInfo,Certificate,Skill
# Register your models here.

admin.site.register(CV)
admin.site.register(WorkExperience)
admin.site.register(BasicInfo)
admin.site.register(Certificate)
admin.site.register(Skill)
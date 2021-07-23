from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.Home,name='home'),
    path('about/',views.About,name='about'),
    path('skills/',views.Skills,name='skills'),
    path('experience/',views.Work_experience,name='work_experience'),
    path('education/',views.Education,name='education'),
    path('contact/',views.Contact,name='contact'),
    path('certificate/',views.CertificateInfo,name='certificate'),

]
urlpatterns +=static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
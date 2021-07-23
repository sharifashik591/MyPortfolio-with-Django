from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from project import views
urlpatterns=[
    path('project/',views.project_detail,name='project_detail'),
    path('project/data_analysis/',views.Data_Analysis,name='data_analysis'),
    path('project/MachineLearning/',views.MachineLearning,name='MachineLearning'),
    path('project/DeepLearning/',views.DeepLearning,name='DeepLearning'),
    path('project/WebDevelopment/',views.Webdevelopment,name='WebDevelopment'),

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
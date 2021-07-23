# Generated by Django 3.2.3 on 2021-07-19 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_catagory', models.CharField(choices=[('Data Analysis', 'Data Analysis'), ('Machine Learning', 'Machine Learning'), ('Deep Learning', 'Deep Learning'), ('Web Development', 'Web Development')], max_length=100)),
                ('project_description', models.TextField()),
                ('project_url', models.URLField()),
                ('project_pic', models.ImageField(blank=True, upload_to='project_img')),
            ],
        ),
    ]

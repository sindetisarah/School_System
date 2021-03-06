# Generated by Django 3.2.5 on 2021-07-29 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('second_name', models.CharField(max_length=12)),
                ('age', models.PositiveSmallIntegerField()),
                ('nationality', models.CharField(max_length=12)),
                ('date_of_birth', models.CharField(max_length=12)),
                ('class_name', models.CharField(max_length=15)),
                ('national_id', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('admission_date', models.DateField()),
                ('academic_year', models.IntegerField(max_length=4)),
                ('students_contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('guardians_contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('room_number', models.CharField(max_length=12)),
                ('health_report', models.FileField(upload_to='')),
                ('profile_image', models.ImageField(upload_to='')),
                ('username', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=1000)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

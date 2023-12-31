# Generated by Django 4.1 on 2023-10-21 09:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0008_jobposting_jobapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='company_profile_pics/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])]),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='student_profile_pics/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])]),
        ),
    ]

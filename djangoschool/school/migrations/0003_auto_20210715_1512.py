# Generated by Django 3.0 on 2021-07-15 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20210713_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allstudent',
            old_name='othe',
            new_name='other',
        ),
        migrations.AddField(
            model_name='allstudent',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='studentphoto'),
        ),
    ]

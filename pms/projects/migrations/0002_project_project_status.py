# Generated by Django 4.2.10 on 2024-03-17 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_status',
            field=models.CharField(choices=[('Active', 'Active'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('On Hold', 'On Hold')], default='Active', max_length=50),
        ),
    ]

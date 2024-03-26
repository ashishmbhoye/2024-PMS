# Generated by Django 4.2.10 on 2024-03-16 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technology', models.CharField(choices=[('Python', 'Python'), ('Java', 'Java'), ('C++', 'C++'), ('C#', 'C#')], max_length=100)),
                ('estimated_hours', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('complateion_date', models.DateField()),
            ],
            options={
                'db_table': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Project_module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('estimated_hours', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'db_table': 'project_module',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('priority', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Not Started', 'Not Started'), ('Progress', 'Progress'), ('complteted', 'complteted')], max_length=50)),
                ('estimated_minutes', models.PositiveIntegerField()),
                ('total_util_time', models.PositiveIntegerField()),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project_module')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='User_task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taksid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.task')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project_team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'project_team',
            },
        ),
    ]

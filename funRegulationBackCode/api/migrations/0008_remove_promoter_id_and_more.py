# Generated by Django 4.2 on 2023-09-11 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_results', '0003_auto_20181106_1101'),
        ('api', '0007_remove_project_created_by_remove_project_removed_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectanalysisregistry',
            name='download_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectanalysisregistry',
            name='download_organism',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectanalysisregistry',
            name='task_download_organism',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_celery_results.taskresult'),
        ),
    ]

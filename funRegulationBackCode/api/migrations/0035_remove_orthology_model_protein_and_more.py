# Generated by Django 4.2 on 2023-10-01 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_remove_protein_unique_protein_protein_unique_protein'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orthology',
            name='model_protein',
        ),
        migrations.RemoveField(
            model_name='orthology',
            name='target_protein',
        ),
        migrations.AddField(
            model_name='orthology',
            name='model_protein',
            field=models.ManyToManyField(related_name='ort_protein_model_protein', to='api.protein'),
        ),
        migrations.AddField(
            model_name='orthology',
            name='target_protein',
            field=models.ManyToManyField(related_name='ort_protein_target_protein', to='api.protein'),
        ),
    ]

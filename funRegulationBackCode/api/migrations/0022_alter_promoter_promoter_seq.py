# Generated by Django 4.2 on 2023-09-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_promoter_strand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promoter',
            name='promoter_seq',
            field=models.TextField(blank=True, null=True),
        ),
    ]

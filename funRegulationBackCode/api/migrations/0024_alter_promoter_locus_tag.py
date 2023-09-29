# Generated by Django 4.2 on 2023-09-25 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_promoter_locus_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promoter',
            name='locus_tag',
            field=models.ForeignKey(blank=True, db_column='locus_tag', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.gene'),
        ),
    ]

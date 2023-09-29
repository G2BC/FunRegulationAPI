# Generated by Django 4.2 on 2023-09-25 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_alter_promoter_promoter_seq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promoter',
            name='locus_tag',
            field=models.OneToOneField(blank=True, db_column='locus_tag', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.gene'),
        ),
        migrations.AlterField(
            model_name='promoter',
            name='organism_accession',
            field=models.ForeignKey(db_column='organism_accession', on_delete=django.db.models.deletion.DO_NOTHING, related_name='prot_organism_accession', to='api.gene'),
        ),
    ]
# Generated by Django 4.2 on 2023-10-01 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_alter_modelregulatory_organism_accession_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orthology',
            name='model_locus_tag',
            field=models.ForeignKey(db_column='model_locus_tag', default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ort_model_locus_tag', to='api.gene'),
        ),
        migrations.AlterField(
            model_name='orthology',
            name='target_locus_tag',
            field=models.ForeignKey(db_column='target_locus_tag', default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ort_target_locus_tag', to='api.gene'),
        ),
        migrations.AlterField(
            model_name='tfbs',
            name='organism_accession',
            field=models.ForeignKey(blank=True, db_column='organism_accession', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tfbs_gene_organism_accession', to='api.organism'),
        ),
    ]
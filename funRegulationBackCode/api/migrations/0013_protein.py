# Generated by Django 4.2 on 2023-09-24 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_gene'),
    ]

    operations = [
        migrations.CreateModel(
            name='Protein',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('product', models.CharField(blank=True, max_length=255, null=True)),
                ('interpro', models.CharField(blank=True, max_length=255, null=True)),
                ('pfam', models.CharField(blank=True, max_length=255, null=True)),
                ('go', models.CharField(blank=True, max_length=255, null=True)),
                ('gene3d', models.CharField(blank=True, max_length=255, null=True)),
                ('reactome', models.CharField(blank=True, max_length=255, null=True)),
                ('panther', models.CharField(blank=True, max_length=255, null=True)),
                ('uniprot', models.CharField(blank=True, max_length=255, null=True)),
                ('ec_number', models.CharField(blank=True, max_length=255, null=True)),
                ('cazy', models.CharField(blank=True, max_length=255, null=True)),
                ('uniparc', models.CharField(blank=True, max_length=255, null=True)),
                ('locus_tag', models.ForeignKey(blank=True, db_column='locus_tag', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='prot_gene_locus_tag', to='api.gene')),
                ('organism_accession', models.ForeignKey(blank=True, db_column='organism_accession', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='prot_gene_organism_accession', to='api.gene')),
            ],
            options={
                'db_table': 'protein',
            },
        ),
    ]

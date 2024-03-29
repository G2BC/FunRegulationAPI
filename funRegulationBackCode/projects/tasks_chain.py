from celery import shared_task, chain
from django.conf import settings
from django.db import transaction
from django_celery_results.models import TaskResult

from funRegulationTool.task_utils import FunRegulationBaseTask
from projects.tasks_import import task_import_genes
from projects.tasks_external_tools import task_run_proteinortho, task_run_rsat
from projects.tasks_calc_centrality import *
from api.models import ProjectAnalysisRegistry

def analyse_registry(registry):
    if registry is None or type(registry) is not ProjectAnalysisRegistry:
        raise ValueError('registry should be an instance of ProjectAnalysisRegistry')
    result = task_analyse_registry.apply_async((registry.pk,)) 
    registry.task = TaskResult.objects.get(task_id=result.task_id)
    registry.save()

@shared_task(bind=True, name='analyse_registry', base=FunRegulationBaseTask)
def task_analyse_registry(self, registry_id):
    registry = ProjectAnalysisRegistry.objects.get(pk=registry_id)
    with transaction.atomic():
        if registry.download_organism and registry.proteinortho_analyse and registry.rsat_analyse:
            #chain(task1.s(),chord([task2.s(), task3.s()], immutable=True),task4.s()).delay()
            chain(task_import_genes.si(registry_id, registry.organism_accession) | 
                  task_run_proteinortho.si(registry_id, registry.organism_accession) |
                  task_run_create_graph.si(registry_id, registry.organism_accession) |
                  task_degree_centrality.s(registry_id, registry.organism_accession) | 
                  task_closeness_centrality.s(registry_id, registry.organism_accession) | 
                  task_betweenness_centrality.s(registry_id, registry.organism_accession) | 
                  task_eigenvector_centrality.s(registry_id, registry.organism_accession) | 
                  task_harmonic_centrality.s(registry_id, registry.organism_accession) | 
                  task_run_rsat.si(registry_id, registry.organism_accession)
                  ).apply_async()
        elif registry.download_organism and registry.proteinortho_analyse:
            chain(task_import_genes.si(registry_id, registry.organism_accession) |
                  task_run_proteinortho.si(registry_id, registry.organism_accession) |
                  task_run_create_graph.si(registry_id, registry.organism_accession) |
                  task_degree_centrality.s(registry_id, registry.organism_accession) | 
                  task_closeness_centrality.s(registry_id, registry.organism_accession) | 
                  task_betweenness_centrality.s(registry_id, registry.organism_accession) | 
                  task_eigenvector_centrality.s(registry_id, registry.organism_accession) | 
                  task_harmonic_centrality.s(registry_id, registry.organism_accession)
                 ).apply_async()
        registry.save()
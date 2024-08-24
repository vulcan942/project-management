from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProjectModel
from ..config.neo4j import neo4j_connection
from ..utils.generate_embeddings import generate_embedding

@receiver(post_save, sender=ProjectModel)
def store_project_embeddings(sender,instance:ProjectModel,**kwargs) -> None:
    print("saving embeddings")
    project_context = instance.description
    project_embedding = generate_embedding(project_context)

    # Query: why are we doing this?
    project_embedding_str = ",".join(map(str,project_embedding))

    query = """
    MERGE (p:Project {project_id:$project_id})
    SET p.name = $project_name,
        p.embedding = $project_embedding
    """
    parameters = {
        "project_id": instance.id,
        "project_name": instance.name,
        "project_embedding": project_embedding_str
    }

    neo4j_connection.execute_query(query,parameters)
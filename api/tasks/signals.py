from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TaskModel
from ..config.neo4j import neo4j_connection
from ..utils.generate_embeddings import generate_embedding

@receiver(post_save, sender=TaskModel)
def store_task_embeddings(sender,instance:TaskModel,**kwargs) -> None:
    task_context = instance.description
    task_title_embedding = generate_embedding(instance.title)
    task_description_embedding = generate_embedding(task_context)

    task_embedding = task_title_embedding + task_description_embedding

    # Query: why are we doing this?
    task_embedding_str = ",".join(map(str,task_embedding))

    query = """
    MERGE (t:Task {task_id:$task_id})
    SET t.embedding = $task_embedding
        t.name = $task_name
        t.sprint_id = $sprint_id
    """
    parameters = {
        "task_id": instance.id,
        "sprint_id": instance.sprint.id,
        "task_name": instance.name,
        "task_embedding": task_embedding_str
    }

    neo4j_connection.execute_query(query,parameters)
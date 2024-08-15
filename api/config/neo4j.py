from neo4j import GraphDatabase
from django.conf import settings
class Neo4jConnection:
    def __init__(self,uri,user,password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()
    
    def execute_query(self,query,parameters=None):
       with self.driver.session as session:
           result = session.run(query,parameters)
           return result
       
neo4j_connection = Neo4jConnection(settings.NEO4J_CONNECTION_STRING,user=settings.NEO4J_USER,password=settings.NEO4J_PASSWORD)
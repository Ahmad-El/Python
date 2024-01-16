from neo4j import GraphDatabase
import json

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "1234567890")
with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
    
# Get the name of all 42 year-olds
    records, summary, keys = driver.execute_query(
        # "MATCH (p:Person {age: $age}) RETURN p.name AS name",
        "MATCH (n) RETURN n LIMIT 25",
        database_="neo4j",
    )
    # for record in records:
    #     print(record.data())
    
    
    with driver.session() as session:
        with open("link1.json", "r") as file:
            json_data = json.load(file)
            query = """
                UNWIND $json_data AS root
                MERGE (rootNode:Node {id: root.key})
                WITH rootNode, root.value AS nested
                UNWIND [key IN keys(nested) | {key: key, value: nested[key]}] AS links
                FOREACH (link IN links |
                    MERGE (childNode:Node {id: link.value.key})
                    MERGE (rootNode)-[:HAS_LINK]->(childNode)
                )
            """
            

            session.run(query, json_data=json_data)    
    driver.close()
    
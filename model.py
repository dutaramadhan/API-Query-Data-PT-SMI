import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

load_dotenv()

db_params = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_DATABASE'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': os.getenv('DB_PORT'),
}

def vector_search(query_vector, limit=10):
  conn = psycopg2.connect(**db_params)
  cursor = conn.cursor()
  sql_query = """
    SELECT 
        (embedding <#> %s) * -1 AS similarity,
        data.id,
        source_title,
        content
    FROM data
    JOIN source_metadata ON data.source_id = source_metadata.id
    WHERE embedding IS NOT NULL
    ORDER BY similarity DESC
    LIMIT %s;
  """

  # Execute the query with the Python array as a parameter
  cursor.execute(sql_query, (str(query_vector), limit))
  data = cursor.fetchall()
  cursor.close()
  conn.close()

  return data
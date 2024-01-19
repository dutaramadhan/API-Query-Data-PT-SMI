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

def vector_search_content(query_vector, limit=5):
  conn = psycopg2.connect(**db_params)
  cursor = conn.cursor()
  sql_query = """
    SELECT 
        (embedding <#> %s) * -1 AS similarity,
        data.id,
        source_title,
        content,
        total_tokens
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

def vector_search_header(query_vector, limit=5):
  conn = psycopg2.connect(**db_params)
  cursor = conn.cursor()
  sql_query = """
    SELECT 
        (header_embedding <#> %s) * -1 AS similarity,
        data.id,
        source_title,
        content,
        total_tokens
    FROM data
    JOIN source_metadata ON data.source_id = source_metadata.id
    WHERE header_embedding IS NOT NULL
    ORDER BY similarity DESC
    LIMIT %s;
  """

  # Execute the query with the Python array as a parameter
  cursor.execute(sql_query, (str(query_vector), limit))
  data = cursor.fetchall()
  cursor.close()
  conn.close()

  return data

def vector_search(query_vector, limit=10):
  conn = psycopg2.connect(**db_params)
  cursor = conn.cursor()

  # Calculate similarity using the inner product of vectors
  computed_similarity = """
    SELECT 
      (header_embedding <#> %s) * -1 AS similarity_header,
      (embedding <#> %s) * -1 AS similarity_content,
      id,    
      content,
      total_tokens,
      source_id
    FROM data
    WHERE embedding IS NOT NULL
  """
  # Select most similar data
  sql_query = """
    SELECT 
      GREATEST(similarity_header, similarity_content) AS similarity,
      data.id,
      source_title,
      content,
      total_tokens,
      similarity_header,
      similarity_content
    FROM ({}) AS data
    JOIN source_metadata ON data.source_id = source_metadata.id
    ORDER BY similarity DESC
    LIMIT %s;
  """.format(computed_similarity)

  # Execute the query 
  cursor.execute(sql_query, (str(query_vector), str(query_vector), limit))
  data = cursor.fetchall()
  cursor.close()
  conn.close()

  return data
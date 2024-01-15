import psycopg2
from psycopg2 import sql
import os

db_params = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_DATABASE'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': os.getenv('DB_PORT')
}

def vector_search(query_vector, limit=3):
  conn = psycopg2.connect(**db_params)
  cursor = conn.cursor()
  sql_query = """
SELECT
    SUM(data.embedding[i] * query) AS similarity,
    data.id,
    source_title,
    data.content 
FROM
    data
JOIN
    unnest(%s) WITH ORDINALITY arr(query, i) ON true
JOIN
    source_metadata ON data.source_id = source_metadata.id
WHERE
    embedding IS NOT NULL
GROUP BY
    data.id, source_title, data.content  -- Include all non-aggregated columns in GROUP BY
ORDER BY
    similarity DESC
LIMIT %s;
  """

  # Execute the query with the Python array as a parameter
  cursor.execute(sql_query, (query_vector, limit))
  data = cursor.fetchall()
  cursor.close()
  conn.close()

  return data
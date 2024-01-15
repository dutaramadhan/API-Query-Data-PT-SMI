from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from openai import OpenAI
import psycopg2
import model

app = Flask(__name__)
load_dotenv()
client = OpenAI(api_key = os.getenv('API_KEY'))

def get_embedding(text):
   response = client.embeddings.create(
    input = text,
    model="text-embedding-ada-002"
    )
   return response

@app.route('/smi/api/embedding/query', methods=['GET'])
def get_data():
    query = request.args.get('query')
    query_embedding = get_embedding(query)
    query_vector = query_embedding.data[0].embedding
    results = model.vector_search(query_vector)
    
    response_data = []
    for result in results:
        entry = {
            "similarity": result[0],
            "id": result[1],
            "source_title": result[2],
            "content": result[3]
        }
        response_data.append(entry)

    response_data = {"result": response_data}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from openai import OpenAI
import psycopg2
import model
import json
import requests

app = Flask(__name__)
load_dotenv()
client = OpenAI(api_key = os.getenv('API_KEY'))

def get_embedding(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response

@app.route('/smi/api/embedding/query', methods=['GET'])
def get_data():
    query = request.args.get('query')
    try:
        response = get_embedding(query)

        if "error" in query:
            raise Exception(response.error.message)
        
        query_vector = response.data[0].embedding
        results = model.vector_search(query_vector) + model.vector_search_header(query_vector)
        response_data = []  
        for result in results:
            entry = {
                "similarity": result[0],
                "id": result[1],
                "source_uri": result[2],
                "source_title": result[3],
                "content": result[4],
                "total_tokens": result[5],
            }
            response_data.append(entry)

        response_data = {"result": response_data}
        return jsonify(response_data)
    
    except Exception as e:
        return jsonify({"error": str(e)}) 

@app.route('/')
def info():
    return 'Server is Running on port ' + os.getenv('APP_PORT') 

if __name__ == '__main__':
    app.run(debug=False)

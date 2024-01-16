from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
#from openai import OpenAI
import psycopg2
import model
import json
import requests

app = Flask(__name__)
load_dotenv()
#client = OpenAI(api_key = os.getenv('API_KEY'))

def get_embedding(text):
   response = client.embeddings.create(
    input = text,
    model="text-embedding-ada-002"
    )
   return response

def getEmbeddings(text):
    url = "https://api.openai.com/v1/embeddings"

    payload = json.dumps({
        "input": text,
        "model": "text-embedding-ada-002",
        "encoding_format": "float"
    })
    headers = {
        'Authorization': 'Bearer ' + os.getenv('API_KEY'),
        'Content-Type': 'application/json',
        'Cookie': '__cf_bm=Ghr17uXmAZAP3sAagI5nlm2Ex4fSgiGKZGkREvPnsOw-1704772804-1-AUlILWecFQtgsKkszWgeW2iUzF6M/ai9qRJVSxnA0/NP7bCdqWX4CmsGjo4F6UP7n382NwuTgTNV/RWe2GfcqEM=; _cfuvid=1fYoJQCnpqqs.xdVCMebdMShJREPBmizEhyzPI.C9cE-1704772804555-0-604800000'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()

@app.route('/smi/api/embedding/query', methods=['GET'])
def get_data():
    query = request.args.get('query')
    try:
        query_embedding = getEmbeddings(query)
        query_vector = query_embedding['data'][0]['embedding']
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
    except Exception as e:
        return e 

if __name__ == '__main__':
    app.run(debug=False)

from flask import Flask
from app import create_app
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

app = Flask(__name__)

app.config.update(
    API_KEY=os.getenv('API_KEY'),
    DB_HOST=os.getenv('DB_HOST'),
    DB_DATABASE=os.getenv('DB_DATABASE'),
    DB_USER=os.getenv('DB_USER'),
    DB_PASSWORD=os.getenv('DB_PASSWORD'),
    DB_PORT=os.getenv('DB_PORT')
)

if __name__ == '__main__':
    app.run(debug=True)

<h1 align="center"> Query API </h1>

## Information About this API
API ini berfungsi untuk melakukan query atau retrieval data dari database. Pengguna akan memberikan input berupa teks yang kemudian input tersebut akan di-embedding dan hasil dari embedding tersebut digunakan untuk mencari simmilarity antara input dengan semua data yang ada di database. API akan memberikan output berupa 10 buah data yang terdiri dari 5 data yang content-nya memiliki nilai simmilarity paling tinggi dengan input dan 5 data yang header-nya memiliki nilai simmilarity paling tinggi dengan input.

## Our Main Feature
### 1. Embedding Text
Input teks dari user di-embedding menggunakan model "text-embedding-ada-002" dari OpenAI yang menghasilkan output berupa embedding vector dengan dimensi 1536 dan memiliki panjang vector 1 (ternormalisasi).
### 2. Vector Search
Hasil embedding dari input user akan di-dot product dengan embedding vector dari content dan header setiap data yang ada pada database. Hasil dot product tersebut menghasilkan simmilarity antara input user dengan setiap content dan header dari data yang ada pada database. Nilai simmilarity input dengan content dan header diurutkan dari nilai terbesar hingga terkecil. Hasilnya diambil 5 data dengan nilai simmilarity content terbesar dan 5 data dengan nilai simmilarity header terbesar.

## Tech Stack
### 1. Python
### 2. Flask
### 3. OpenAI
### 4. Postgresql
### 5. pgvector
### 6. Docker

## How to Set Up
### 1. Postgresql
### 2. pgvector
Untuk lebih detailnya bisa dilihat pada <a href='https://github.com/pgvector/pgvector'>repositori github pgvector</a>

## How to Run Locally
1. Clone repositori ini
   ```
   git clone https://github.com/dutaramadhan/API-Query-Data-PT-SMI.git
   ```
2. Buka direktori API-Query-Data-PT-SMI
3. Install pyhton virtual environtment 
   ```
   pip install virtualenv
   ```
4. Buat virtual environment
   ```
   virtualenv venv
   ```
6. Aktifkan virtual environment
   - Windows
     ```
     venv/Scripts/activate
     ```
   - Linux/macOS
     ```
     source venv/bin/activate
     ```
7. Install semua library atau depedensi yang dibutuhkan
   ```
   pip install -r requirements.txt
   ```
8. Buat file .env
   ```
   API_KEY = ...
   DB_HOST = ... 
   DB_DATABASE = ...
   DB_USER = ...
   DB_PASSWORD = ...
   DB_PORT = ...
   APP_PORT = ...
   ```
9. Jalankan aplikasi
   ```
   python app.py
   ```
10. Cek apakah server sedang berjalan
    ```
    http://localhost:5000/
    ```

## How to Deploy
1. Buat file .env
   ```
      API_KEY = ...
      DB_HOST = ... 
      DB_DATABASE = ...
      DB_USER = ...
      DB_PASSWORD = ...
      DB_PORT = ...
      APP_PORT = ...
   ```
2. Build docker image
   ```
   docker build -t api-query .
   ```
3. Run docker image
   ```
   docker run -d -p 5000:5000 --name api-query api-query
   ```
4. Cek apakah server sedang berjalan
    ```
    http://<ip-host>:5000/
    ```
## API Endpoint
 - ##### Route
   ```
   GET /smi/api/embedding/query
   ```

- ##### Parameters
  ```
  query: string
  ```



<h1 align="center"> Query API </h1>

## Information About this API
API ini berfungsi untuk melakukan query atau retrieval data dari database. User akan memberikan input berupa teks yang kemudian input tersebut akan di-embedding dan hasil dari embedding tersebut digunakan untuk mencari simmilarity antara input dengan semua data yang ada di database. API akan memberikan response berupa 10 buah data yang terdiri dari 5 data yang content-nya memiliki nilai simmilarity paling tinggi dengan input dan 5 data yang header-nya memiliki nilai simmilarity paling tinggi dengan input. Response tersebut di-deliver kepada user dalam format JSON.

## Our Main Feature
### 1. Embedding Text
Input teks dari user di-embedding menggunakan model "text-embedding-ada-002" dari OpenAI yang menghasilkan output berupa embedding vector dengan dimensi 1536 dan memiliki panjang vector 1 (ternormalisasi).
### 2. Vector Search
Hasil embedding dari input user akan di-dot product dengan embedding vector dari content dan header setiap data yang ada pada database. Hasil dot product tersebut menghasilkan simmilarity antara input user dengan setiap content dan header dari data yang ada pada database. Nilai simmilarity input dengan content dan header diurutkan dari nilai terbesar hingga terkecil. Hasilnya diambil 5 data dengan nilai simmilarity content terbesar dan 5 data dengan nilai simmilarity header terbesar.

## Alur Sistem
![Alur Sistem](https://drive.google.com/uc?id=14XjApjDHPmihbtRHg-LN9Ac9ZzBmiVTL)
1. Sistem API Query menerima input berupa query (string)
2. Fetch request ke API OpenAI dengan query (string) sebagai masukan untuk proses embedding
3. Hasil embedding diperoleh berupa vektor berdimensi 1536
4. Vector digunakan untuk search data ke database berdasarkan vector similarity (dot product antara vektor query dan vektor data)
5. Diperoleh beberapa data yang relevan
6. Data dikembalikan sebagai response

## Tech Stack
### 1. Python
### 2. Flask
### 3. OpenAI
### 4. Postgresql
### 5. pgvector
### 6. Docker

## How to Set Up
### 1. Postgresql
Skema database
```
CREATE TABLE IF NOT EXISTS public.source_metadata
(
    source_uri character varying,
    source_name character varying,
    source_title character varying,
    created_at timestamp without time zone DEFAULT now(),
    id SERIAL NOT NULL,
    CONSTRAINT source_metadata_pkey PRIMARY KEY (id)
)
```
```
CREATE TABLE IF NOT EXISTS public.data
(
    content text,
    total_tokens integer,
    source_id integer,
    id SERIAL NOT NULL,
    embedding vector(1536),
    header_embedding vector(1536),
    CONSTRAINT data_pkey PRIMARY KEY (id),
    CONSTRAINT source FOREIGN KEY (source_id)
        REFERENCES public.source_metadata (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
```
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
  
- ##### Response
  ```
  {
     "result": [
        {
           "content": string,
           "id": int,
           "similarity": double,
           "source_title": string,
           "source_uri": string,
           "total_tokens": int
        }
     ]
  }
  ```

## Related Repository
- <a href='https://github.com/dutaramadhan/API-Otomasi-ETL-PT-SMI'>API-Otomasi-ETL-PT-SMI</a>


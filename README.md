<h1 align="center"> Query API </h1>

## Information About this API
API ini berfungsi untuk melakukan query atau retrieval data dari database. Pengguna akan memberikan input berupa teks yang kemudian input tersebut akan di-embedding dan hasil dari embedding tersebut digunakan untuk mencari simmilarity antara input dengan semua data yang ada di database. API akan memberikan output berupa 10 buah data yang terdiri dari 5 data yang content-nya memiliki nilai simmilarity paling tinggi dengan input dan 5 data yang header-nya memiliki nilai simmilarity paling tinggi dengan input.

## Our Main Feature
### 1. Embedding Text
Input teks dari user akan di-embedding menggunakan model "text-embedding-ada-002" dari OpenAI yang menghasilkan output berupa embedding vector dengan dimensi 1536 dan memiliki panjang vector 1 (dinormalisasi).
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

## How to Deploy

## API Endpoint
 - ##### Route
   ```
   GET /smi/api/embedding/query
   ```

- ##### Parameters
  ```
  query: string
  ```



## Overview
Project ini berisi proses pengambilan data dari Google BigQuery, analisis outlier pada kolom harga retail, pembersihan data, dan pembuatan API sederhana menggunakan FastAPI untuk menampilkan data yang sudah dibersihkan.

Dataset yang digunakan diambil dari public dataset BigQuery:
- **Project**: `bigquery-public-data`
- **Dataset**: `iowa_liquor_sales`
- **Table**: `sales`

Kolom yang dianalisis:
- `state_bottle_retail`

Filter yang digunakan pada pengambilan data:
- `vendor_name = 'SAZERAC COMPANY  INC'`

Jumlah data yang diambil:
- `LIMIT 5000`

## Objectives
Project ini dikerjakan untuk:
- mengambil data dari Google BigQuery menggunakan SQL
- menghitung central tendency pada data harga retail
- mengecek distribusi data melalui skewness
- mendeteksi outlier dengan metode IQR
- membuat dataset bersih tanpa outlier
- menampilkan hasil data bersih melalui FastAPI

## Workflow
### 1. Data Extraction
Data diambil dari Google BigQuery menggunakan query SQL berikut:

```sql
SELECT state_bottle_retail
FROM `bigquery-public-data.iowa_liquor_sales.sales`
WHERE vendor_name = 'SAZERAC COMPANY  INC'
LIMIT 5000
```

### 2. Statistical Analysis
Analisis yang dilakukan pada data awal:
- mean
- median
- mode
- skewness

Hasil analisis digunakan untuk melihat kecenderungan pemusatan data dan bentuk distribusinya.

### 3. Outlier Detection
Outlier dideteksi menggunakan **IQR (Interquartile Range)**:
- hitung Q1 dan Q3
- hitung IQR = Q3 - Q1
- tentukan batas bawah dan batas atas
- data di luar rentang dianggap outlier

Berdasarkan notebook, persentase outlier yang ditemukan adalah **0.36%**.

### 4. Data Cleaning
Setelah outlier dihapus, data bersih disimpan ke file CSV untuk digunakan kembali pada API.

### 5. API Development
API dibuat menggunakan **FastAPI** untuk menampilkan data hasil cleaning.

Endpoint yang tersedia:
- `/` → pesan utama API
- `/data` → menampilkan seluruh data bersih
- `/data/{row_id}` → menampilkan data berdasarkan indeks baris

## Files
- `P0LC3_Ali_Abdurrahman.ipynb` → notebook utama berisi query, analisis statistik, deteksi outlier, dan visualisasi
- `P0LC3_Ali Abdurrahman_app.py` → script FastAPI
- `P0LC3_Ali Abdurrahman_data_clean.csv` → data hasil cleaning
- `README.md` → penjelasan project

## Tech Stack
- Python
- Pandas
- Google BigQuery
- SQL
- FastAPI
- Matplotlib
- Seaborn

## Notes for Interview
Kalau project ini dibahas saat interview, poin yang bisa ditekankan:
- pernah melakukan query data langsung dari **Google BigQuery**
- menggunakan **SQL** untuk mengambil data sesuai kebutuhan
- melakukan analisis distribusi dan outlier sebelum data dipakai
- membuat **data cleaning output** dalam CSV
- membangun **API sederhana** untuk menyajikan data hasil cleaning

## Suggested Repository / Folder Name
Kalau mau disimpan rapi di local, nama folder yang aman dan profesional:
- `bigquery-anomaly-analysis-api`
- `lc3-bigquery-outlier-api`
- `retail-price-anomaly-api`

Yang paling netral dan enak dipakai:
**`bigquery-anomaly-analysis-api`**

"""Membuat API (Section 2)"""

from fastapi import FastAPI
import pandas as pd

# Membuat instance dari FastAPI
app = FastAPI()

# Load data hasil cleaning outlier (data_clean.csv) ke dalam Data Frame

df = pd.read_csv("P0LC3_Ali Abdurrahman_data_clean")

@app.get("/")
def home():
    """
    Endpoint utama (root) API.
    Digunakan untuk menguji apakah API sedang berjalan dan memberikan respons default.
    
    Returns:
        dict: Pesan sambutan sederhana.
    """
    return {"message": "API Anomali Harga Retail - Data Bersih"}

@app.get("/data")
def get_all_data():
    """
    Endpoint untuk mengambil seluruh data bersih hasil pembersihan outlier.
    Data akan dikonversi ke dalam bentuk list of dictionary agar bisa di-encode ke format JSON.

    Returns:
        list: Seluruh data bersih dalam format JSON array of records.
    """
    return df.to_dict(orient="records")

@app.get("/data/{row_id}")
def get_data_by_row(row_id: int):
    """
    Endpoint untuk mengambil satu baris data berdasarkan indeks (baris ke-N).
    
    Args:
        row_id (int): Indeks baris yang ingin diambil (dimulai dari 0).

    Returns:
        dict: Data baris sesuai row_id jika ditemukan.
        dict: Pesan error jika indeks berada di luar jangkauan.
    """
    if row_id >= len(df):
        return {"error": "Index tidak ditemukan"}
    return df.iloc[row_id].to_dict()

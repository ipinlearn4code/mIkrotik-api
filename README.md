Berikut adalah dokumentasi lengkap untuk API Python MikroTik yang dapat Anda tambahkan ke file README di GitHub.

---

# MikroTik PPP Secret API Service

API ini menyediakan endpoint untuk mengelola `ppp secret` pada perangkat MikroTik, termasuk operasi CRUD, enable, dan disable. Setiap endpoint membutuhkan autentikasi berbasis API key.

## Prasyarat

- **Python** (versi 3.7+)
- **MikroTik Router** dengan akses API aktif
- **Flask** dan **librouteros** library
  ```bash
  pip install Flask librouteros
  ```

## Konfigurasi

1. Buat file konfigurasi di `src/config/config.py` dan tambahkan pengaturan untuk koneksi MikroTik dan API key Anda:

   ```python
   # src/config/config.py

   # Konfigurasi MikroTik
   MIKROTIK_IP = '192.168.88.1'        # Ganti dengan IP MikroTik Anda
   MIKROTIK_USERNAME = 'admin'         # Ganti dengan username MikroTik Anda
   MIKROTIK_PASSWORD = 'password'      # Ganti dengan password MikroTik Anda
   MIKROTIK_PORT = 8728                # Port API MikroTik (default 8728)

   # API Key untuk autentikasi
   API_KEY = 'your_api_key_here'
   ```

2. **File Struktur Proyek**:
   ```
   project_folder/
   ├── src/
   │   ├── config/
   │   │   └── config.py            # File konfigurasi, termasuk pengaturan MikroTik dan API key
   │   ├── core/
   │   │   ├── models/
   │   │   │   └── ppp_secret_model.py    # Model untuk ppp_secret
   │   │   └── services/
   │   │       └── ppp_secret_service.py  # Service untuk CRUD dan operasi lainnya
   ├── main.py                     # File utama untuk menjalankan aplikasi
   ```

## Menjalankan API

Jalankan API dengan perintah:

```bash
python main.py
```

API akan berjalan di `http://127.0.0.1:5000`.

## Dokumentasi Endpoint

### Autentikasi API

Semua endpoint memerlukan autentikasi berbasis API key. Anda dapat menyertakan API key dengan dua cara:
1. Sebagai header: `x-api-key`
2. Sebagai parameter URL: `?api_key=your_api_key_here`

### Endpoint

#### 1. Menambahkan PPP Secret

- **URL**: `/ppp-secret`
- **Method**: `POST`
- **Headers**: 
  - `x-api-key`: API key Anda
- **Body**:
  ```json
  {
    "name": "testuser",
    "password": "testpass",
    "profile": "default"
  }
  ```
- **Response**:
  - **201 Created**:
    ```json
    {
      "message": "PPP Secret 'testuser' created successfully."
    }
    ```
  - **400 Bad Request**:
    ```json
    {
      "error": "Name, password, and profile are required"
    }
    ```

#### 2. Membaca PPP Secret Berdasarkan Nama

- **URL**: `/ppp-secret/<name>`
- **Method**: `GET`
- **Headers**: 
  - `x-api-key`: API key Anda
- **Response**:
  - **200 OK**: Mengembalikan data `ppp secret` yang diminta
  - **404 Not Found**:
    ```json
    {
      "error": "PPP Secret 'testuser' not found"
    }
    ```

#### 3. Membaca Semua PPP Secret

- **URL**: `/ppp-secret`
- **Method**: `GET`
- **Headers**: 
  - `x-api-key`: API key Anda
- **Response**:
  - **200 OK**: Mengembalikan daftar semua `ppp secret`

#### 4. Memperbarui PPP Secret

- **URL**: `/ppp-secret/<name>`
- **Method**: `PUT`
- **Headers**: 
  - `x-api-key`: API key Anda
- **Body** (opsional):
  ```json
  {
    "password": "newpass",
    "profile": "newprofile"
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "message": "PPP Secret 'testuser' updated successfully."
    }
    ```
  - **404 Not Found**:
    ```json
    {
      "error": "PPP Secret 'testuser' not found"
    }
    ```

#### 5. Menonaktifkan PPP Secret

- **URL**: `/ppp-secret/<name>/disable`
- **Method**: `POST`
- **Headers**: 
  - `x-api-key`: API key Anda
- **Response**:
  - **200 OK**:
    ```json
    {
      "message": "PPP Secret 'testuser' disabled successfully."
    }
    ```
  - **404 Not Found**:
    ```json
    {
      "error": "PPP Secret 'testuser' not found"
    }
    ```

#### 6. Mengaktifkan PPP Secret

- **URL**: `/ppp-secret/<name>/enable`
- **Method**: `POST`
- **Headers**: 
  - `x-api-key`: API key Anda
- **Response**:
  - **200 OK**:
    ```json
    {
      "message": "PPP Secret 'testuser' enabled successfully."
    }
    ```
  - **404 Not Found**:
    ```json
    {
      "error": "PPP Secret 'testuser' not found"
    }
    ```

#### 7. Menghapus PPP Secret

- **URL**: `/ppp-secret/<name>`
- **Method**: `DELETE`
- **Headers**: 
  - `x-api-key`: API key Anda
- **Response**:
  - **200 OK**:
    ```json
    {
      "message": "PPP Secret 'testuser' deleted successfully."
    }
    ```
  - **404 Not Found**:
    ```json
    {
      "error": "PPP Secret 'testuser' not found"
    }
    ```

### Contoh Permintaan (Request)

#### Menggunakan `cURL`

1. **Menambahkan PPP Secret**:
   ```bash
   curl -X POST http://127.0.0.1:5000/ppp-secret -H "Content-Type: application/json" -H "x-api-key: your_api_key_here" -d "{\"name\":\"testuser\", \"password\":\"testpass\", \"profile\":\"default\"}"
   ```

2. **Membaca Semua PPP Secret**:
   ```bash
   curl -X GET http://127.0.0.1:5000/ppp-secret -H "x-api-key: your_api_key_here"
   ```

3. **Menonaktifkan PPP Secret**:
   ```bash
   curl -X POST http://127.0.0.1:5000/ppp-secret/testuser/disable -H "x-api-key: your_api_key_here"
   ```

### Menggunakan API dari Browser

Jika Anda ingin mengakses API dari browser, tambahkan API key sebagai parameter URL, misalnya:

```
http://127.0.0.1:5000/ppp-secret?api_key=your_api_key_here
```

---

Dokumentasi ini memberikan panduan lengkap untuk penggunaan API. Pastikan untuk mengganti `your_api_key_here` dengan API key yang valid dari konfigurasi Anda.

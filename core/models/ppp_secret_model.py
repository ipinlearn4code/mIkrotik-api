# core/models/ppp_secret_model.py
from librouteros import connect
from config.mikrotik_config import MIKROTIK_IP, MIKROTIK_USERNAME, MIKROTIK_PASSWORD, MIKROTIK_PORT

class PPPSecret:
    def __init__(self):
        self.api = self.connect_to_mikrotik()

    def connect_to_mikrotik(self):
        """Koneksi ke MikroTik menggunakan konfigurasi dari config.py"""
        try:
            api = connect(
                username=MIKROTIK_USERNAME,
                password=MIKROTIK_PASSWORD,
                host=MIKROTIK_IP,
                port=MIKROTIK_PORT
            )
            return api
        except Exception as e:
            print(f"Failed to connect to MikroTik: {e}")
            return None

    def get_api_path(self):
        """Mengembalikan path untuk ppp/secret"""
        if self.api:
            return self.api.path('ppp/secret')
        return None

    def close_connection(self):
        """Menutup koneksi ke MikroTik"""
        if self.api:
            self.api.close()

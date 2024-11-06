# core/services/ppp_secret_service.py
from core.models.ppp_secret_model import PPPSecret

class PPPSecretService:
    def __init__(self):
        self.ppp_secret_model = PPPSecret()

    def create(self, name, password, profile):
        """Menambahkan PPP Secret"""
        api_path = self.ppp_secret_model.get_api_path()
        if api_path:
            api_path.add(name=name, password=password, profile=profile)
            print(f"PPP Secret '{name}' created successfully.")

    def read(self, name):
        """Membaca PPP Secret berdasarkan nama"""
        api_path = self.ppp_secret_model.get_api_path()
        if api_path:
            for secret in api_path:
                if secret.get('name') == name:
                    return secret
            print(f"No PPP Secret found with name '{name}'")
        return None

    def read_all(self):
        """Membaca semua PPP Secret"""
        api_path = self.ppp_secret_model.get_api_path()
        secrets = []
        if api_path:
            for secret in api_path:
                secrets.append(secret)
            return secrets
        print("No PPP Secrets found.")
        return secrets

    def update(self, name, new_password=None, new_profile=None):
        """Memperbarui PPP Secret berdasarkan nama"""
        api_path = self.ppp_secret_model.get_api_path()
        if api_path:
            for secret in api_path:
                if secret.get('name') == name:
                    secret_id = secret['.id']
                    updates = {}
                    if new_password:
                        updates['password'] = new_password
                    if new_profile:
                        updates['profile'] = new_profile
                    api_path.update(id=secret_id, **updates)
                    print(f"PPP Secret '{name}' updated successfully.")
                    return True
            print(f"No PPP Secret found with name '{name}'")
        return False

    def delete(self, name):
        """Menghapus PPP Secret berdasarkan nama"""
        api_path = self.ppp_secret_model.get_api_path()
        if api_path:
            for secret in api_path:
                if secret.get('name') == name:
                    secret_id = secret['.id']
                    api_path.remove(secret_id)
                    print(f"PPP Secret '{name}' deleted successfully.")
                    return True
            print(f"No PPP Secret found with name '{name}'")
        return False

    def enable(self, name):
        """Mengaktifkan PPP Secret berdasarkan nama"""
        api_path = self.ppp_secret_model.get_api_path()
        if api_path:
            for secret in api_path:
                if secret.get('name') == name:
                    secret_id = secret['.id']
                    api_path.update(id=secret_id, disabled='no')
                    print(f"PPP Secret '{name}' enabled successfully.")
                    return True
            print(f"No PPP Secret found with name '{name}'")
        return False

    def disable(self, name):
        """Menonaktifkan PPP Secret berdasarkan nama"""
        api_path = self.ppp_secret_model.get_api_path()
        if api_path:
            for secret in api_path:
                if secret.get('name') == name:
                    secret_id = secret['.id']
                    api_path.update(id=secret_id, disabled='yes')
                    print(f"PPP Secret '{name}' disabled successfully.")
                    return True
            print(f"No PPP Secret found with name '{name}'")
        return False

    def close(self):
        """Menutup koneksi"""
        self.ppp_secret_model.close_connection()
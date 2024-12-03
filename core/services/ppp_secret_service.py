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
        """Memperbarui PPP Secret berdasarkan nama dengan menggunakan read()"""
        # Use read() method to get the secret by name
        secret = self.read(name)
        
        if secret.values():
            secret_id = secret['.id']  # Ensure you're using the correct ID field

            # Prepare the fields to update
            updates = {}
            
            if new_password:
                updates['password'] = new_password
            if new_profile:
                updates['profile'] = new_profile
            if new_password or new_profile:
                updates['.id'] = secret_id
            if not updates:
                print("No fields to update.")
                return False

            # Use 'call()' to update the secret
            try:
                # params = {'.id' :'*7', 'password': new_password, 'profile': new_profile}
                # Perform the update using call() with the 'set' operation
                api_path = self.ppp_secret_model.get_api_path()  # Ensure this is the correct path object
                api_path.update(**updates)  # Update using the 'set' operation

                print(f"PPP Secret '{name}' updated successfully.")
                return True
            except Exception as e:
                print(f"Error updating PPP Secret '{name}': {e}")
                return False
        else:
            print(f"No PPP Secret found with name '{name}'")
            return False


    
    # def update(self, name, new_password=None, new_profile=None):
    #     """Memperbarui PPP Secret berdasarkan nama"""
    #     api_path = self.ppp_secret_model.get_api_path()
    #     if api_path:
    #         for secret in api_path:
    #             if secret.get('name') == name:
    #                 secret_id = secret['.id']
    #                 updates = {}
    #                 if new_password:
    #                     updates['password'] = new_password
    #                 if new_profile:
    #                     updates['profile'] = new_profile
    #                 api_path.update(id=secret_id, **updates)
    #                 print(f"PPP Secret '{name}' updated successfully.")
    #                 return True
    #         print(f"No PPP Secret found with name '{name}'")
    #     return False

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
                    updates = {'disabled': False, '.id' : secret_id}
                    api_path.update(**updates)
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
                    updates = {'disabled': True, '.id' : secret_id}
                    api_path.update(**updates)
                    print(f"PPP Secret '{name}' disabled successfully.")
                    return True
            print(f"No PPP Secret found with name '{name}'")
        return False

    def close(self):
        """Menutup koneksi"""
        self.ppp_secret_model.close_connection()

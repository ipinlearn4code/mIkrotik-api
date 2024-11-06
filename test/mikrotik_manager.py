from librouteros import connect
# from librouteros.exceptions import RouterOsApiConnectionError

# Konfigurasi MikroTik
MIKROTIK_IP = '103.217.216.34'
MIKROTIK_USERNAME = 'cahganteng'
MIKROTIK_PASSWORD = 'asalkampung'
MIKROTIK_PORT = 8928           

def connect_to_mikrotik():
    """Fungsi untuk menghubungkan ke MikroTik"""
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
    
def read_all_ppp_secrets():
    api = connect_to_mikrotik()
    if api:
        ppp_secrets = api.path('ppp/secret')
        all_secrets = []
        for secret in ppp_secrets:
            all_secrets.append(secret)
        api.close()
        
        # Menampilkan semua data ppp secret
        if all_secrets:
            for secret in all_secrets:
                print(secret)
        else:
            print("No PPP Secrets found.")

# Fungsi CRUD untuk PPP Secret
def create_ppp_secret(name, password, profile):
    api = connect_to_mikrotik()
    if api:
        api.path('ppp/secret').add(name=name, password=password, profile=profile)
        print(f"PPP Secret '{name}' created successfully.")
        api.close()

def read_ppp_secret(name):
    api = connect_to_mikrotik()
    if api:
        ppp_secrets = api.path('ppp/secret')
        found = False
        for secret in ppp_secrets:
            if secret.get('name') == name:
                print(secret)
                found = True
                break
        if not found:
            print(f"No PPP Secret found with name '{name}'")
        api.close()


def update_ppp_secret(name, new_password=None, new_profile=None):
    api = connect_to_mikrotik()
    if api:
        ppp_secrets = api.path('ppp/secret')
        found = False
        for secret in ppp_secrets:
            if secret.get('name') == name:
                id = secret['.id']
                updates = {}
                if new_password:
                    updates['password'] = new_password
                if new_profile:
                    updates['profile'] = new_profile
                ppp_secrets.update(id=id, **updates)
                print(f"PPP Secret '{name}' updated successfully.")
                found = True
                break
        if not found:
            print(f"No PPP Secret found with name '{name}'")
        api.close()


def delete_ppp_secret(name):
    api = connect_to_mikrotik()
    if api:
        ppp_secrets = api.path('ppp/secret')
        found = False
        for secret in ppp_secrets:
            if secret.get('name') == name:
                secret_id = secret['.id']
                ppp_secrets.remove(secret_id)  # Kirim secret_id sebagai positional argument
                print(f"PPP Secret '{name}' deleted successfully.")
                found = True
                break
        if not found:
            print(f"No PPP Secret found with name '{name}'")
        api.close()



# Fungsi untuk Enable/Disable PPP Secret
def enable_ppp_secret(name):
    api = connect_to_mikrotik()
    if api:
        ppp_secrets = api.path('ppp/secret')
        found = False
        for secret in ppp_secrets:
            if secret.get('name') == name:
                secret_id = secret['.id']
                params = {
                    'disabled': False,  # False untuk mengaktifkan
                    '.id': secret_id
                }
                ppp_secrets.update(**params)
                print(f"PPP Secret '{name}' enabled successfully.")
                found = True
                break
        if not found:
            print(f"No PPP Secret found with name '{name}'")
        api.close()

def disable_ppp_secret(name):
    api = connect_to_mikrotik()
    if api:
        ppp_secrets = api.path('ppp/secret')
        found = False
        for secret in ppp_secrets:
            if secret.get('name') == name:
                secret_id = secret['.id']
                params = {
                    'disabled': True,  # True untuk menonaktifkan
                    '.id': secret_id
                }
                ppp_secrets.update(**params)
                print(f"PPP Secret '{name}' disabled successfully.")
                found = True
                break
        if not found:
            print(f"No PPP Secret found with name '{name}'")
        api.close()



# Contoh penggunaan fungsi
if __name__ == "__main__":
    # Tambahkan secret baru
    # create_ppp_secret(name="alpincobaAPI", password="testpass", profile="default")
    
    # Baca data secret
    # read_ppp_secret(name="alpincobaAPI")
    
    # # Update secret
    # update_ppp_secret(name="testuser", new_password="newpass", new_profile="default")
    
    # # Nonaktifkan secret
    # disable_ppp_secret(name="alpincobaAPI")
    
    # # Aktifkan secret
    # enable_ppp_secret(name="alpincobaAPI")
    
    # # Hapus secret
    # delete_ppp_secret(name="alpincobaAPI")
    read_all_ppp_secrets()
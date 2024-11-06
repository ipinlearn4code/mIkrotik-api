from librouteros import connect
from librouteros.exceptions import TrapError

# Replace with your MikroTik credentials and IP
username = 'cahganteng'
password = 'asalkampung'
router_ip = '103.217.216.34'  # Replace with your MikroTik Router IP
port = 8928  # Default port for the API

try:
    # Connect to MikroTik router
    api = connect(username=username, password=password, host=router_ip, port=port)
    print("Connected successfully to MikroTik API!")

    # Fetch PPP Secrets using .get()
    ppp_secrets = api.path('queue', 'simple')

    # Print each secret
    for secret in ppp_secrets:
        print(secret)

except TrapError as e:
    print(f"API Error: {e}")

except Exception as e:
    print(f"Failed to connect: {e}")

import socket
import requests
def get_external_ip():
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
        print(f"\nLocal IP: {local_ip}")

        external_ip = requests.get('https://api64.ipify.org?format=json').json()['ip']
        print(f"Public IP: {external_ip}")

    except Exception as e:
        print(f"Hata: {e}")

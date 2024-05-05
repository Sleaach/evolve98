import uuid
def mac():
    try:
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
        print(f"MAC Adresi: {mac}")
    except Exception as e:
        print(f"Hata oluştu: {e}")

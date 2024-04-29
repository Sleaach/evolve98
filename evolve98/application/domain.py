import whois
def domain_checker():
    try:
        domain = input("Domain: ")
        
        domain_info = whois.whois(domain)

        print("Domain Bilgileri:")
        print(f"Domain Adı: {domain_info.domain_name}")
        print(f"Oluşturulma Tarihi: {domain_info.creation_date}")
        print(f"Son Güncelleme Tarihi: {domain_info.last_updated}")
        print(f"Bitiş Tarihi: {domain_info.expiration_date}")

        if domain_info.status:
            print("Durumlar:")
            for status in domain_info.status:
                print(f"  - {status}")

    except whois.parser.PywhoisError as e:
        print(f"Hata: {e}")

import phonenumbers
from phonenumbers import carrier 
from opencage.geocoder import OpenCageGeocode
from phonenumbers import geocoder as pn_geocoder  

def numcheck():
    Key = "6d6f969fd9024ac8afde957f0c86a5ba"
    number = input("GSM: ")

    check_number = phonenumbers.parse(number)

    number_location = pn_geocoder.description_for_number(check_number, "en")
    print(number_location)

    service = carrier.name_for_number(check_number, "en")
    print(service)

    geocoder_api = OpenCageGeocode(Key)  
    query = str(number_location)
    results = geocoder_api.geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print("Konum", lat, lng)

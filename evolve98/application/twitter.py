from requests_oauthlib import OAuth1Session
import json
def twt():
 print("'twthelp' kodunu çalıştırıp okuduğunuzdan emin olun.\n")
 consumer_key = input("API: ")
 consumer_secret = input("SECRET: ")
 mesaj = input("Post: ")
 payload = {"text": mesaj}

 request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
 oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

 try:
    fetch_response = oauth.fetch_request_token(request_token_url)
 except Exception as e:
   print(f"Bir hata oluştu: {e}")

 resource_owner_key = fetch_response.get("oauth_token")
 resource_owner_secret = fetch_response.get("oauth_token_secret")
 print("OAuth jetonunu aldım: %s" % resource_owner_key)



 base_authorization_url = "https://api.twitter.com/oauth/authorize"
 authorization_url = oauth.authorization_url(base_authorization_url)
 print("Lütfen buraya gidin ve yetkilendirin: %s" % authorization_url)
 verifier = input("PIN'i buraya yapıştırın: ")


 access_token_url = "https://api.twitter.com/oauth/access_token"
 oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
 oauth_tokens = oauth.fetch_access_token(access_token_url)

 access_token = oauth_tokens["oauth_token"]
 access_token_secret = oauth_tokens["oauth_token_secret"]

 oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

 response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
)

 if response.status_code != 201:
    raise Exception(
        "İstek bir hata döndürdü: {} {}".format(response.status_code, response.text)
    )

 print("Cevap kodu: {}".format(response.status_code))


 json_response = response.json()
 print(json.dumps(json_response, indent=4, sort_keys=True))

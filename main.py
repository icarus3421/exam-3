
print("Hello World")

import requests

client_id = "YbZa3BuNGihrDSTJ"
client_secret = "94b36afb72124a69a74c5380e78b5f09"

token = requests.post('https://www.arcgis.com/sharing/rest/oauth2/token/', params={
  'f': 'json',
  'client_id': client_id,
  'client_secret': client_secret,
  'grant_type': 'client_credentials',
  'expiration': '1440'
})

print(token.json()['access_token']);

u = requests.Session()

data = u.post('http://geoenrich.arcgis.com/arcgis/rest/services/World/GeoenrichmentServer/Geoenrichment/enrich', params={
  'f': 'json',
  'token': token.json()['access_token'],
  'studyAreas': '[{"geometry":{"x":-117.1956,"y":34.0572}}]'
})

print(data.json())
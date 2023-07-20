import requests

response = requests.get(url="http://kanye.rest")  # latlong.net for get position on map
# print(response.status_code)
response.raise_for_status()

all_data = response.json()
data = response.json()["iss_position"]
print(all_data)
print(data)
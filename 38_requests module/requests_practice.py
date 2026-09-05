import requests
response = requests.get('https://api.github.com')
print(response.status_code)

import requests
response = requests.get('https://api.github.com')
data = response.json()
print(data)

import requests
print("==== REQUESTS MODULE PRACTICE ====")

response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)

data = response.json()

print("API Name;", data["current_user_url"])
import requests

response = requests.get("https://www.stackoverflow.com")

print(response.status_code)
print(response.reason)  
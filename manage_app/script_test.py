import requests

resp = requests.get("http://127.0.0.1:8000/api/roles")
print(resp.status_code)
# print(resp.content.decode())
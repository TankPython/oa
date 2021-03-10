import requests
import json

resp = requests.get("http://127.0.0.1:8000/api/roles?pagenum=2&pagesize=4&query=t")
data = json.loads(resp.content.decode())
print(data)
print(len(data["data"]["results"]))

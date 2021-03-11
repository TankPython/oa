import requests
import json

# 获取
# resp = requests.get("http://127.0.0.1:8000/api/role?pagenum=1&pagesize=5&query=t&id=1")
# data = json.loads(resp.content.decode())
# print(data)


# 注册
# resp = requests.post("http://127.0.0.1:8000/api/register/",data={"na6me":"tan1","password":"123456"})
# data = json.loads(resp.content.decode())
# print(data)


# # 修改角色
# resp = requests.post("http://127.0.0.1:8000/api/role/", data={"name": "6656", "id": 1})
# data = json.loads(resp.content.decode())
# print(data)

# 修改角色
resp = requests.put("http://127.0.0.1:8000/api/role/", data={"id": 1})
data = json.loads(resp.content.decode())
print(data)

import json

# with open("./dataList.json") as f:
#     print(json.loads(f.read()))



result = json.loads('{"username":"david.wei","token":"QFIdEKqb71ZLeJyXT0vh3uAVZLQvVRd9"}')
json.dumps()

print(type(result), result["username"])

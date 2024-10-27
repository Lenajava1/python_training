import json

with open("c:\\Users\\ilyas\\test\\config.json") as f:
    try:
        res = json.load(f)
    except ValueError as ex:
        print(ex)
        res = {}

print(res)
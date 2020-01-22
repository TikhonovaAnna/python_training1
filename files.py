import json

with open("C://Users//Anna//PycharmProjects/config.json") as f:
    try:
        res = json.load(f)
    except ValueError as ex:
        print(ex)
        res = ()

print(res)
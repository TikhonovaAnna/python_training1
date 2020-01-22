import json

f = open("C://Users//Anna//PycharmProjects/config.json")
try:
    res = json.load(f)
except ValueError as ex:
    print(ex)
    res = ()
finally:
    f.close()

print(res)
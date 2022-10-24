import json
from pprint import pprint

data = '''
{
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}'''

data = json.loads(data)
for k, v in data.items():
    for k1, v1 in v.items():
        v[k1] = type(v1).__name__

pprint(data)

# 'str' > str
# extension "Paste JSON as Code" https://marketplace.visualstudio.com/items?itemName=quicktype.quicktype
# запускается как Ctrl+Shift+P (Cmd+Shift+P on MacOS)

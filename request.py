import requests

def requestURL(URL):
    url = "http://192.168.41.111:6011/uploadDocument/front/"

    payload = {}
    files=[
    ('file',('my_ct_front.jpg',open('/home/sushil/Documents/my_ct_front.jpg','rb'),'image/jpeg'))
    ]
    headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2OTE0Mjk1ODgsImlhdCI6MTY3NTg3NzI4OCwic3ViIjoiZG90bmV0In0.xEZrifwMLBVSyz812yOqxLXuzXfTXgLKchREgYG1J-U'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    response.text
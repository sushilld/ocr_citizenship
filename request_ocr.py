import requests

def requestURL(url, image):
    # url = "http://192.168.41.111:6011/uploadDocument/front/"
    print('Request Received')
    payload = {}
    files = {
        'file': (image.name, image.read(), 'image/jpeg')
    }
    headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2OTE0Mjk1ODgsImlhdCI6MTY3NTg3NzI4OCwic3ViIjoiZG90bmV0In0.xEZrifwMLBVSyz812yOqxLXuzXfTXgLKchREgYG1J-U'
    }
    try:
        response = requests.post(url, headers=headers, data=payload, files=files)
        response_text = response.json()
    except:
        response_text = {'status': 'error', 'message': 'OCR Server is down. Try again later.', 'info': None}
    # print(response_text)
    return response_text
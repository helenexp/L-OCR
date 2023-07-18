import base64

import requests


class Bookworm:
    def __init__(self, url):
        self.url = url

    def get_text(self, image_file):
        content = base64.b64encode(image_file.read())
        response = requests.post(self.url, data=content, headers={'Content-Type': 'application/octet-stream'})
        return response.json()

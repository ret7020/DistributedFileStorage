import requests
import os

class Client:
    def __init__(self, main_server):
        self.main_server = main_server

    def send_file(self, file_path):
        files = {'file': open(file_path,'rb')}
        #req = requests.post(self.main_server, files=files)
        req = requests.post(self.main_server, data={"file_size": os.path.getsize(file_path)})
        return req.status_code

if __name__ == "__main__":
    client = Client('http://localhost:8080/api/upload_file')
    result = client.send_file("data.txt")
    print(result)


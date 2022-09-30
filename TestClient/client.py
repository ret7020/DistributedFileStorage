import requests


class Client:
    def __init__(self, main_server):
        self.main_server = main_server

    def send_file(self):
        files = {'upload_file': open('data.txt','rb')}

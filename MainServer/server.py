from flask import Flask, jsonify, request
from db import DataBase
from utils import allowed_file
from config import *
import requests
import json

class WebApi:
    def __init__(self, name, host='0.0.0.0', port=8080):
        self.app = Flask(name)
        self.host = host
        self.port = port
        self.app.config["TEMPLATES_AUTO_RELOAD"] = True
        with open("hostings.json") as hosting_list_file:
            self.hostings_list = json.load(hosting_list_file)
    
        @self.app.route('/')
        def __index():
            return self.index()

        @self.app.route('/api/upload_file', methods=['POST'])
        def __upload_file():
            return self.upload_file()

        @self.app.route('/api/load_file')
        def __load_file():
            return self.index()
    
    def index(self):
        return "Main Server Index Page"

    def upload_file(self):
        for hosting in self.hostings_list:
            data = requests.get(f"{hosting}/api/server_status").json()
            if data:
                print(data)

        

    
    def run(self):
        self.app.run(host=self.host, port=self.port)

if __name__ == "__main__":
    web = WebApi(__name__)
    web.run()

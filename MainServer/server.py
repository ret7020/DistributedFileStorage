from flask import Flask, jsonify
from db import DataBase

class WebApi:
    def __init__(self, name, host='0.0.0.0', port=8080):
        self.app = Flask(name)
        self.host = host
        self.port = port
        self.app.config["TEMPLATES_AUTO_RELOAD"] = True
    
        @self.app.route('/')
        def __index():
            return self.index()

        @self.app.route('/api/upload_file', method=['POST'])
        def __upload_file():
            return self.upload_file()

        @self.app.route('/api/load_file')
        def __load_file():
            return self.index()
    
    def index(self):
        return "Main Server Index Page"

    def upload_file(self):
        pass
        

    
    def run(self):
        self.app.run(host=self.host, port=self.port)

if __name__ == "__main__":
    web = WebApi(__name__)
    web.run()

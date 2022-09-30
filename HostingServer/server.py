from flask import Flask, jsonify, request
from config import *

class WebApi:
    def __init__(self, name, host='0.0.0.0', port=8080):
        self.app = Flask(name)
        self.host = host
        self.port = port
        self.app.config["TEMPLATES_AUTO_RELOAD"] = True
    
        @self.app.route('/')
        def __index():
            return self.index()

        @self.app.route('/api/upload_file')
        def __upload_file():
            return self.upload_file()

        @self.app.route('/api/load_file')
        def __load_file():
            return self.index()

        @self.app.route('/api/server_status')
        def __server_status():
            return self.server_status()
    
    def index(self):
        return f"Hosting #{CURRENT_INSTANCE_ID}"

    def upload_file(self):
        data = request.files
        print(data)
        return jsonify({"status": True})

    def server_status():
        return jsonify({"": ""})
    
    def run(self):
        self.app.run(host=self.host, port=self.port)

if __name__ == "__main__":
    web = WebApi(__name__, host=MAIN_SERVER_HOST)
    web.run()

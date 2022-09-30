from flask import Flask, jsonify, request
from config import *
from random import randint

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
        if 'file' in request.files:
            data_file = request.files['file']
            if allowed_file(data_file.filename, ALLOWED_EXTENSIONS):
                binary_data = data_file.read()
                return jsonify({"status": True})
            else:
                return jsonify({"status": False})
        else:
            return jsonify({"status": False, "data": "No file uploaded"})
        data = request.files['file'].read()
        filename = f"{randint(10 ** 5, 10 ** 10)}{int(time.time())}{randint(10 ** 5, 10 ** 10)}."
        return jsonify({"status": True})

    def server_status():
        return jsonify({"": ""})
    
    def run(self):
        self.app.run(host=self.host, port=self.port)

if __name__ == "__main__":
    web = WebApi(__name__, host=MAIN_SERVER_HOST)
    web.run()

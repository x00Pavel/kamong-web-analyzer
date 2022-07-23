from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import time

app = Flask(__name__)
api = Api(app)


class Hello(Resource):

    def get(self):
        return jsonify({
            "server_ip": request.host,
            "ip": request.remote_addr,
            "ts": time.time()})

api.add_resource(Hello, "/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8008)
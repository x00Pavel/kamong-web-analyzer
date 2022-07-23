from base64 import encode
from webbrowser import get
from flask import Flask, request, jsonify, json
from flask_restful import Resource, Api
from kafka import KafkaProducer
import time
from os import getenv
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
api = Api(app)

KAFKA_BOOTSTRAP_SERVER_NAME = getenv("KAFKA_BOOTSTRAP_SERVER_NAME")
KAFKA_PORT = getenv("KAFKA_PORT")

assert KAFKA_BOOTSTRAP_SERVER_NAME is not None
assert KAFKA_PORT is not None

TOPIC_NAME = getenv("TOPIC_NAME")
KAFKA_SERVER = f"{KAFKA_BOOTSTRAP_SERVER_NAME}:{KAFKA_PORT}"

app.logger.debug(f"Kafka topic: {TOPIC_NAME}")
app.logger.debug(f"Kafka bootstrap server: {KAFKA_SERVER}")

producer = KafkaProducer(
    bootstrap_servers = KAFKA_SERVER,
    api_version = (0, 11, 15)
)


class Hello(Resource):

    def get(self):
        
        data = {
            "server_ip": request.host,
            "ip": request.remote_addr,
            "ts": time.time()}
        json_paylaod = json.dumps(data)
        
        producer.send(TOPIC_NAME, json_paylaod.encode("utf-8"))
        producer.flush()

        app.logger.debug(f"Parsed data to kafka: {json_paylaod}")

        return jsonify(data)

api.add_resource(Hello, "/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8008)
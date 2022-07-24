#!/bin/sh
curl -X POST -H "Content-Type: application/json" --data @/sinc-connector.json http://connect:8083/connectors -w "\n"
# print all connectors added to kafka connect
curl -X GET http://connect:8083/connectors

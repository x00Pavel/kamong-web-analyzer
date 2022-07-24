# Web analyzer using Apache Kafka and MongoDb

## TLDR

To setup whole environment run following commands

```bash
docker-compose up -d  # starts all containers
docker exec shell bash /initialize-container.sh  # creates Kafka connector for MongoDb
```

To see results from MongoDB collection run

```
docker exec -ti mongo1 mongosh mongodb://mongo1:27017/web-analyzer
db.activity.find().pretty()
```

## Detailed description

The task is solved and solution is demonstrated using containers and corresponding technologies.
> :warning: during development and testing **podman-compose** was used instead of **docker-compose**

[`docker-compose.yaml`](docker-compose.yaml) file contains a list of following services (containers):

- *zookeeper* and *broker* services are necessary building blocks for Apache Kafka
- *init-kafka* container for crating the topic on the broker (Kafka) server
- *connect* starts Apache Kafka Connect service and install plugin (connector) for MongoDb
- *mongo1* MongoDb instance
- *mongo1-setup* container for configuring MongoDb instance
- *shell* container that is used to manipulate with broker server and to send REST API calls to connect service.
- *flask* minimal Flask web that send events to the broker
- *user1/user2/user3* containers that simulates the traffic for server via accessing it using curl

### Interconnection

This section describes the data flow in this environment.

Flask web app is running on the address http://localhoost:8008 and has only one
page - root page "/". Users try to access this page using following command

```bash
curl http://localhost:8008
```

> In user's container this command is running in `while true` loop to 
> simulate constant traffic

The user receives following response in JSON format:

```json
{
  "destination": "http://127.0.0.1:8008/", 
  "source_ip": "10.89.0.7", 
  "ts": 1658671538.7909791
}
```

where:

- *destination* is a destination URL from the request
- *source_ip* source IP address from which the request was made
- *ts* time stamp of the request (when the server received request)

Along with sending the reply to the client, the server send same data to the
Apache Kafka running on address `broker:29029` to the `my-topic` Kafka topic.
> Port 29029 is specified for accessing the Kafka server in containers default
> network. To access the same data from the local machine use address `localhost:9029`

There is Apache Kafka Connector for MongoDb that is listening on the topic
`my-topic`.
As soon as the new event arrives, the connector pulls data, serialise it and
pushs to the MongoDb `web-activity` database using `analyzer` collection.

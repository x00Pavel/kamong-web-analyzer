// create config for primary replica
var conf = {
    _id: "rs0",
    members:[{_id : 0, host : "mongo1:27017"}]
}
var err = rs.initiate(conf)
print(err)
print(rs.config())

db = db.getSiblingDB("web-analyzer");
db.createCollection("activity");

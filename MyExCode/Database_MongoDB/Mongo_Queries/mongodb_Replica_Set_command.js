cfg = {
  "_id": "RS",
  "members": [{
      "_id": 0,
      "host": "172.105.39.26:31141"
    },
    {
      "_id": 1,
      "host": "172.105.39.26:31142",
      // 以下是實作 Secondary-Only
      "votes": 0,
      "priority": 0
    },
    {
      "_id": 2,
      "host": "172.105.39.26:31143",
      "votes": 0,
      "priority": 0
    }
  ]
};
// 建立 Replica_Set
rs.initiate(cfg);

// 返回包含當前副本集 配置的文檔。
rs.conf()
// 返回包含當前副本集 配置的文檔。
// https://docs.mongodb.com/manual/reference/method/rs.conf/#mongodb-method-rs.conf
// {
//     _id: <string>,
//     version: <int>,
//     term: <int>,
//     protocolVersion: <number>,
//     writeConcernMajorityJournalDefault: <boolean>,
//     configsvr: <boolean>,
//     members: [
//       {
//         _id: <int>,
//         host: <string>,
//         arbiterOnly: <boolean>,
//         buildIndexes: <boolean>,
//         hidden: <boolean>,
//         priority: <number>,
//         tags: <document>,
//         secondaryDelaySecs: <int>,
//         votes: <number>
//       },
//       ...
//     ],
//     settings: {
//       chainingAllowed : <boolean>,
//       heartbeatIntervalMillis : <int>,
//       heartbeatTimeoutSecs: <int>,
//       electionTimeoutMillis : <int>,
//       catchUpTimeoutMillis : <int>,
//       getLastErrorModes : <document>,
//       getLastErrorDefaults : <document>,
//       replicaSetId: <ObjectId>
//     }
// }

// 通過指令新增 Replica Set 節點
rs.add("172.105.39.26:31142")
rs.add("mongodb-a3:27019")
// 透過 rs.status() 查看 Replica Set 設定狀態
rs.status()
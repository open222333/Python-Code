cfg = {
    "_id": "RS",
    "members": [{
        "_id": 0,
        "host": "172.105.39.26:31141"
    },
    {
        "_id": 1,
        "host": "172.105.39.26:31142"
    },
    {
        "_id": 2,
        "host": "172.105.39.26:31143"
    }
    ]
};
rs.initiate(cfg);

rs.conf()

// 通過指令新增 Replica Set 節點
rs.add("172.105.39.26:31142")
rs.add("mongodb-a3:27019")
// 透過 rs.status() 查看 Replica Set 設定狀態
rs.status()
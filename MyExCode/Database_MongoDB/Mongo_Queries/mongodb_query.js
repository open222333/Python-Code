// 找重複
db.collection
  .aggregate()
  .group({
    _id: '$key',
    count: {
      $sum: 1
    }
  })
  .match({
    count: {
      $gt: 1
    }
  })

db.getCollection('articles').aggregate([{
  $match: {
    $expr: {
      $and: [{
          $gte: [{
            $dateFromString: {
              creationDate: '10-08-2018',
              format: '%m-%d-%Y'
            }
          }]
        },
        {
          $lte: [{
            $dateFromString: {
              creationDate: '10-08-2018',
              format: '%m-%d-%Y'
            }
          }]
        }
      ]
    }
  }
}])

// 使用日期數學返回 BSON 日期：
db.collection.aggregate([{
    $group: {
      _id: {
        $add: [{
            $subtract: [{
                $subtract: ['$date', datetime.datetime.utcfromtimestamp(0)]
              },
              {
                $mod: [{
                    $subtract: ['$date', datetime.datetime.utcfromtimestamp(0)]
                  },
                  1000 * 60 * 60 * 24
                ]
              }
            ]
          },
          datetime.datetime.utcfromtimestamp(0)
        ]
      },
      count: {
        $sum: 1
      }
    }
  },
  {
    $sort: {
      _id: 1
    }
  }
])

// 篩選符合 col1 col2 條件的
db.collection
  .aggregate()
  .match({
    col_name: {
      $elemMatch: {
        col1: null,
        col2: 'a'
      }
    }
  })
  .sort({
    _id: -1
  })
  .count()

// 篩選符合 col_name1 col_name2
db.collection
  .aggregate()
  .match({
    col_name1: {
      $elemMatch: {
        col1: null,
        col2: 'a'
      }
    }
  })
  .project({})
  .match({
    col_name2: {
      $elemMatch: {
        col3: null,
        col4: 'b'
      }
    }
  })
  .sort({
    _id: -1
  })
  .count()
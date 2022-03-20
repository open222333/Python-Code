# 遍歷字典
players = {'Stephen Curry': 'Golden State Warriors',
           'Kevin Durant': 'Golden State Warriors',
           'lebron James': 'Cleveland Cavaliers',
           'James Harden': 'Houston Rockets',
           'Paul Gasol': 'San Antonio Spurs'}
for name, team in players.items():
    print("\n姓名：", name)
    print("隊名：", team)

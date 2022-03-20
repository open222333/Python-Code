# 合併字典 update()
dealerA = {1: 'Nissan', 2: 'Toyota', 3: 'Lexus'}
dealerB = {3: 'BMW', 4: 'Benz'}  # A的3會被覆蓋
dealerA.update(dealerB)
print(dealerA)

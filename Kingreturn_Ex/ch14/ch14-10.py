import os

files = ['ch14_1.py', 'ch14_2.py', 'ch14_3.py']
for file in files:
    print(os.path.join('ch14/', file))

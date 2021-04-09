import json

fn = 'ch21/population.json'
with open(fn) as fileObj:
    datas = json.load(fileObj)

newdata = []
for data in datas:
    if data['Year'] == 2000:
        newdata.append(data)

with open('ch21/out21t_2.json', 'w') as fileObj:
    json.dump(newdata, fileObj)

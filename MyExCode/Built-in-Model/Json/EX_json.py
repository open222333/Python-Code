import json


def create_json_file(data, fileName='data.json'):
    with open(fileName, 'w', newline='') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def trans_to_json(data):
    return json.dumps(data, ensure_ascii=False, indent=4)


data = {
    '001': {
        'test': 1,
        'a': 2,
        'b': "222"
    }
}

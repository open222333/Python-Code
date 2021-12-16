import requests
from flask import request

def get(self):

    # 取得request的值
    msg = request.args.get('msg')
    with Database() as db, db.connect() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                f"SELECT token FROM notify")
            fetch = cur.fetchall()
    for f in fetch:
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f"Bearer {f['token']}"
        }
        payload = {'message': msg}

        r = requests.post(
            'https://notify-api.line.me/api/notify', data=payload, headers=headers)
    return {'result': 'ok'}, 200

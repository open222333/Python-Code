from __future__ import unicode_literals
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

line_bot_api = LineBotApi("9sNHZK9fe++M2HpTjrVMIh60iBvdkEcC+JyJy/hKbrLzOgv7Xu3qXyINBwb9tOEUzCu0NPTSoawQ73opF3fCCcTXO4MqfbJvX7qeJ725UkshQ8BIL9tHQ1BJBYcFNyc/SKFQBIL9tBYcFuX4BYBYC/HQ1BY4BYCYBYC10000000000000000000000000000000004Xu3qXyINBwb9sNHzK9fe++M2HpTjrVMI")
handler = WebhookHandler("2f3748a8f2a08838c3869627c7822d9b")


@app.route("/callback", method=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body:" + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


if __name__ == "__main__":
    app.run()

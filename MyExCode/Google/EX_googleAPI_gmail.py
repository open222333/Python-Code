import os
from googleapiclient._auth import credentials_from_file
from googleapiclient.discovery import build
from google.oauth2 import id_token
from google.auth.transport import requests
'''
OAuth 2.0
https://github.com/googleapis/google-api-python-client/blob/main/docs/oauth.md
https://github.com/googleapis/google-api-python-client/blob/main/docs/start.md'
授權範圍 https://developers.google.com/gmail/api/auth/scopes'''
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
os.chdir(os.path.dirname(__file__))

# 用戶的電子郵件地址。
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gmail_python_token.json'
userId = 'open222333@gmail.com'
url = f'https://gmail.googleapis.com/gmail/v1/users/{userId}/messages'
creds = credentials_from_file('gmail_python_token.json')
service = build('gmail', 'v1', credentials=creds)
results = service.users().messages().list(userId='me').execute()
idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

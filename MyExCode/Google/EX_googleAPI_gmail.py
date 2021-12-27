import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
'''https://github.com/googleapis/google-api-python-client/blob/main/docs/start.md'''

'''
OAuth 2.0
https://github.com/googleapis/google-api-python-client/blob/main/docs/oauth.md

授權範圍 https://developers.google.com/gmail/api/auth/scopes'''
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
os.chdir(os.path.dirname(__file__))


# 用戶的電子郵件地址。
token_file = 'gmail_python_token.json'
userId = 'open222333@gmail.com'
userId = 'me'
url = f'https://gmail.googleapis.com/gmail/v1/users/{userId}/messages'
creds = Credentials.from_authorized_user_file(token_file, SCOPES)
service = build('gmail', 'v1', credentials=creds)

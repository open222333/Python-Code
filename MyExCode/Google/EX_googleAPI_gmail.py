import os
from googleapiclient.discovery import build

'''
OAuth 2.0
https://github.com/googleapis/google-api-python-client/blob/main/docs/oauth.md
https://github.com/googleapis/google-api-python-client/blob/main/docs/start.md'
授權範圍 https://developers.google.com/gmail/api/auth/scopes'''
sc = 'https://www.googleapis.com/auth/gmail.readonly'
SCOPES_2 = ''
os.chdir(os.path.dirname(__file__))


def oauth_service_account(subject):
    '''使用 服務帳戶service_account 進行OAuth驗證
    詳細說明
    https://google-auth.readthedocs.io/en/master/reference/google.oauth2.service_account.html#module-google.oauth2.service_account'''
    from google.oauth2.service_account import Credentials
    filename = 'service-account.json'
    credentials = None
    try:
        credentials = Credentials.from_service_account_file(
            filename,
            scopes=['https://www.googleapis.com/auth/gmail.readonly'],
            subject=subject
        )
    except:
        pass
    return credentials

'''https://stackoverflow.com/questions/42784640/client-is-unauthorized-to-retrieve-access-tokens-using-this-method-gmail-api-c-s/42785468
一般帳號無法使用服務帳號驗證 Gmail API'''
mail = ''
creds = oauth_service_account(mail)
service = build('gmail', 'v1', credentials=creds)
results = service.users().messages().list(userId='me').execute()

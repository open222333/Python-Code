'''OAuth 2.0
https://github.com/googleapis/google-api-python-client/blob/main/docs/oauth.md'''
import os

SCOPES = []


def oauth(token_file):
    '''官方範例 token_file:'''
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from google_auth_oauthlib.flow import InstalledAppFlow

    creds = None
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                token_file, SCOPES)
            creds = flow.run_local_server()
        with open(token_file, 'w') as token:
            token.write(creds.to_json())
    return creds


def oauth_service_account(subject, filename='service-account.json', *scopes):
    '''使用 服務帳戶service_account 進行OAuth驗證
    詳細說明
    https://google-auth.readthedocs.io/en/master/reference/google.oauth2.service_account.html#module-google.oauth2.service_account'''
    from google.oauth2.service_account import Credentials

    credentials = None
    try:
        credentials = Credentials.from_service_account_file(
            filename,
            scopes=[scope for scope in scopes],
            subject=subject
        )
    except:
        pass
    return credentials

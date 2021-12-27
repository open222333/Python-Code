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

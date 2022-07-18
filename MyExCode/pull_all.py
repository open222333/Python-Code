import os
from Git.EX_GitPython import Git
from configparser import ConfigParser

config = ConfigParser()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# os.listdir(os.path.dirname(os.path.abspath(__file__)))
config.read('git_config.ini')
USERNAME = config.get('GIT', 'USERNAME')
PASSWORD = config.get('GIT', 'PASSWORD')
TARGET_DIR = config.get('GIT', 'TARGET_DIR')
GIT_CREDENTIALS_PATH = config.get('GIT', 'GIT_CREDENTIALS_PATH')


def main():
    all_path = os.listdir(TARGET_DIR)
    git_obj = Git()
    git_obj.set_credential_file(
        user=USERNAME,
        token=PASSWORD,
        git_domain='github.com',
        # git config --global credential.helper 'store --file GIT_CREDENTIALS_PATH'
        file_path=GIT_CREDENTIALS_PATH
    )
    for item in all_path:
        git_path = f'{TARGET_DIR}/{item}'
        if os.path.isdir(git_path):
            print(git_path)
            git_obj.set_repo(git_path)
            result = git_obj.do_pull()
            print(f'{item}:{result}\n')


main()

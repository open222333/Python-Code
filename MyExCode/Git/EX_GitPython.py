import git
import os


class Git:
    '''使用git做一個類別'''

    def __init__(self) -> None:
        self.repo = None
        self.user = None
        self.token = None
        self.dir_path = None
        self.git_domain = None

    def set_credential_file(self, user, token, git_domain, file_path):
        '''設定驗證 git_domain: 域名'''
        self.user = user
        self.token = token
        self.git_domain = git_domain
        os.system(f"git config --global credential.helper 'store --file {file_path}'")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f'https://{user}:{token}@{git_domain}\n')

    def set_repo(self, dir_path):
        self.dir_path = dir_path
        if self.is_git_repo():
            self.repo = git.Repo(dir_path)

    def get_remote(self):
        return self.repo.remotes

    def do_pull(self):
        git_action = self.repo.remote()
        result = git_action.pull()
        return [i.__str__() for i in result]

    def do_commit(self):
        pass

    def do_push(self):
        pass

    def is_git_repo(self):
        '''檢查是否為git專案'''
        all_items = os.listdir(self.dir_path)
        return ('.git' in all_items)
    
    def is_commit(self):
        pass

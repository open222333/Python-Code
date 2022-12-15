import os
'''新增 個別git設定 username email config'''


name = "Tom.Li"
email = "open222333@gmail.com"
ingore_dir = ['.vscode']
files = os.listdir()
for file in files:
    if os.path.isdir(file) and file not in ingore_dir:
        file = os.path.abspath(file)
        print(file)
        os.system(f"cd {file} && git config user.name {name}")
        os.system(f"cd {file} && git config user.email {email}")

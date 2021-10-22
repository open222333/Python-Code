time=$(date "+%Y%m%d-%H%M%S")
ssh-add -K ~/.ssh/20210126_forGithub
# ssh-add -K ~/.ssh/20210526_id_ed25519_Email
# pip freeze | tee requirements.txt
# 記錄目前使用的python套件到 requirements.txt
pip list --format=freeze > requirements.txt # 不會有 @ file:// 格式
# git branch a
# git checkout a
git add *
git commit -m"${time}"
# git checkout master
# git merge a # 合併
# git pull # 將上面的拉下來
git push
# git branch -D a

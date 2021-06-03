time=$(date "+%Y%m%d-%H%M%S")
ssh-add -K ~/.ssh/20210126_forGithub
ssh-add -K ~/.ssh/20210526_id_ed25519_Email
git branch a
git checkout a
git add *
git commit -m"${time}"
git checkout master
git merge a
#git pull 
git push
git branch -D a

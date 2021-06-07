time=$(date "+%Y%m%d-%H%M%S")
ssh-add -K ~/.ssh/20210126_forGithub
git branch a
git checkout a
git add *
git commit -m"${time}"
git checkout main
git merge a
# git pull 
git push origin main
git branch -D a

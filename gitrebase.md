if you have some commits in your local branch, and you know the origin branch has some updates since you updated your local branch, now you need to pull the updates and push your local changed to the origin branch.

(1) git fetch origin master

 * branch            master     -> FETCH_HEAD
   43865f9..c3787e6  master     -> origin/master

(2) git status

On branch master
Your branch and 'origin/master' have diverged,
and have 1 and 1 different commit each, respectively.
  (use "git pull" to merge the remote branch into yours)
nothing to commit, working directory clean

(3) git rebase origin master

First, rewinding head to replay your work on top of it...
Applying: common tools

(4) git status

On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

(5) git push origin master


(3)-1 git merge origin master

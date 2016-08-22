| [⬅ 6. Setting up a remote repository in GitHub](06-remotes-in-github.md) | [Table of Contents](00-contents.md) | [8. Dealing with conflicts ➡](08-conflicts.md) |
| :---- |:----:| ----:|

# 7. Collaborating

In section five of this tutorial you learned about branches. We will use branches to collaborate on projects in this class. 

For the next step, get into pairs.  One person will be the "Owner" and the other will be the "Collaborator". The goal is that the Collaborator add changes into the Owner's repository. We will switch roles at the end, so both persons will play Owner and Collaborator.

The Owner needs to give the Collaborator access. On GitHub, click the settings button on the right,
then select Collaborators, and enter your partner's username.

![Adding Collaborators on GitHub](fig/github-add-collaborators.png)

To accept access to the Owner's repo, the Collaborator needs to go to [https://github.com/notifications](https://github.com/notifications).
Once there she can accept access to the Owner's repo.

Next, the Collaborator needs to download a copy of the Owner's repository to her
 machine. This is called "cloning a repo". To clone the Owner's repo into
her `Desktop` folder (for example), the Collaborator enters:

```
$ git clone https://github.com/vlad/planets.git ~/Desktop/vlad-planets
```

Replace 'vlad' with the Owner's username.

![After Creating Clone of Repository](fig/github-collaboration.png)

Now both the Collaborator and the Owner have a local copy of the master branch of the repository. However neither of them should make changes to the master, instead they should work on personal branches. To protect the master from getting unreviewed changes, you can protech your master branch. To do this

1. Owner should navigate to the main page of the repository on github.
2. Under your repository name, click Settings.
3. In the left menu, click Branches.
4  Under Protected Branches, select the master branch.
5. Select Protect this branch, and click Save changes.

Make a branch of your local master and switch to it

```
git branch pluto
git checkout pluto
```

The Collaborator can now make a change in her clone of the Owner's repository,
exactly the same way as we've been doing before:

```
$ cd ~/Desktop/vlad-planets
$ vi pluto.txt
$ cat pluto.txt
It is so a planet!
```

```
$ git add pluto.txt
$ git commit -m "Some notes about Pluto"
 1 file changed, 1 insertion(+)
 create mode 100644 pluto.txt
```


Then push the change to your branch on the *Owner's repository* on GitHub:

```
$ git push origin pluto
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 306 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/vlad/planets.git
   9272da5..29aba7c  pluto -> pluto
```

Take a look to the Owner's repository on its GitHub website now (maybe you need
to refresh your browser.) You should be able to see the new branch made by the
Collaborator.

Now we need to merge the changes. To do this, the Collaborator submits a pull request to the owner. To do this

1. Switch to new branch in Github
2. Click on the new pull request

The Collaborator will then be given a review page that presents you with an overview of the changes, and a place to write a comment. After filling them in you can click `Create pull request`

Now it is the owners job to review the proposed changes. On the owners gitub page, go to the pull requests tab, you should see a new pull request from the contributor. Click on it to review the suggested changes, add comments if necessary.

Once you are ready to merge you can click `Create a merge commit` to merge the branch with master. Both the owner and collaborator can now pull the changes from master to their local copies by entering

```
$ git pull origin master
remote: Counting objects: 4, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0)
Unpacking objects: 100% (3/3), done.
From https://github.com/vlad/planets
 * branch            master     -> FETCH_HEAD
Updating 9272da5..29aba7c
Fast-forward
 pluto.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 pluto.txt
```

Now the three repositories (Owner's local, Collaborator's local, and Owner's on GitHub) are back in sync.

In practice, is is better for the owner to also push to a branch of the 

## A Basic Collaborative Workflow

In practice, it is good to be sure that you have an updated version of the
repository you are collaborating on, so you should `git pull` before making
any changes. The basic collaborative workflow would be:

* update your local repo with `git pull origin master`,
* make your changes and stage them with `git add`,
* commit your changes with `git commit -m`, and
* upload the changes to GitHub with `git push origin master`

It is better to make many commits with smaller changes rather than
of one commit with massive changes: small commits are easier to
read and review.

Note `git pull` is really equivalent to runnign `git fetch` and then `git merge`, where `git fetch` updates your so-called "remote tracking branches" and `git merge` combines the tow brances that were created locally and remotely (the latter is the "origin" branch in the local system nomenclature)

## Switch Roles and Repeat

Switch roles and repeat the whole process.

## Review Changes

The Owner push commits to the repository without giving any information
to the Collaborator. How can the Collaborator find out what has changed with
command line? And on GitHub?

```
git fetch origin
git diff origin master
```

## Comment Changes in GitHub
The Collaborator has some questions about one line change made by the Owner and
has some suggestions to propose.

With GitHub, it is possible to comment the diff of a commit. Over the line of
code to comment, a blue comment icon appears to open a comment window.

The Collaborator posts its comments and suggestions using GitHub interface.

Now comments appear as a bubble in the commits summary. 

| [⬅ 4. Exploring history](04-exploring-history.md) | [Table of Contents](00-contents.md) |  [6. Setting up a remote repository in GitHub ➡](06-remotes-in-github.md) |
| :---- |:----:| ----:|

# 5. Branches

Now we'll learn about git's "killer feature."

Suppose you
"Some people refer to Git’s branching model as its 'killer feature,' and it certainly sets Git apart in the version control community." Unlike other version control systems, Git doesn't actually save changes, but rather full snapshots at each commit step, although it saves disk space by substituting storage pointers for any unchanged files. "When you make a commit, Git stores a commit object that contains a pointer to the snapshot of the content... If you make some changes and commit again, the next commit stores a pointer to the commit that came immediately before it... A branch in Git is simply a lightweight movable pointer to one of these commits. The default branch name in Git is 'master'. As you start making commits, you’re given a master branch that points to the last commit you made. Every time you commit, it moves forward automatically... What happens if you create a new branch? Doing so creates a new pointer for you to move around."

If you create a branch called 'testing' to develop a new feature in your code and switch to the testing branch (in Git-speak, "check it out"), then new commits will move the testing pointer forward instead of the master pointer. Meanwhile you might learn you need to make an urgent change in the master branch -- no problem, you can just take a break from working on 'testing' to check out the master branch and make the urgent change, then commit it and go back to working on the testing branch. Collaborators can work on different branches in the same code development project. After a while each branch contains commits that aren't in the other branches. Git's "merge" command will combine branches into master intelligently, checking for incompatibilities and asking you to fix them.
![The Git Staging Area](fig/git-staging-area.png)

---
layout: page
title: Version Control with Git
subtitle: Branching
minutes: 20?
---
> ## Learning Objectives {.objectives}
>
> *   Explain what branches are and how you might use them in your research.
> *   Create an experimental branch and merge it back in to the master branch.

Often you may want to test out a new feature in some code. You may or may not decide you want to keep this feature and in the mean time you want to make sure you have a version of your script you know works. [Branches](reference#branch) are instances of a repository that can be edited and version controlled in parallel. You can think of it like making an entire copy of your repository folder that you can edit, without affecting the original versions of your scripts. The advantage of using git to do this (rather that making a repo_copy folder on your computer), is that you can use git tools to manage this code while it's under development and you have the ability to seamlessly merge in your changes to your originals.  

To see what branches are available in your repository, you can type `git branch`. First let's make sure we are all in the planets directory in our home folder:

~~~ {.bash}
$ cd ~/planets
$ git branch
~~~

~~~ {.output}
* master
~~~

The master branch is created with the repository is initialized. With an argument, the `branch` command creates a new branch with the given name. Let's make a new experimental branch:

~~~ {.bash}
$ git branch experimental
~~~

~~~ {.output}
  experimental
* master
~~~

The star indicates we are currently in the master branch of our repository. To switch branches, we use the `git checkout` command to checkout a different branch. 

~~~ {.bash}
$ git checkout experimental
$ git branch
~~~

~~~ {.output}
Switched to branch 'experimental'

* experimental
  master
~~~

We have some updated information on pluto, but we aren't sure that we will want to include in our final report. Let's make some updates to the `pluto.txt` file in this experimental branch:

~~~ {.bash}
$ nano pluto.txt
$ cat pluto.txt
~~~

~~~ {.output}
It is so a planet!
A planet with a charming heart on its surface; What's not to love?
~~~

We've made this change on our experimental branch. Let's add and commit this change:

~~~ {.bash}
$ git add pluto.txt
$ git commit -m "Breaking updates about Pluto"
~~~

~~~ {.output}
[experimental c5d6cba] Breaking updates about Pluto
 1 file changed, 1 insertion(+)
~~~

We've committed these changes locally, but we need to push these changes and our new branch to GitHub. To do so, we enter the following command:  

~~~ {.bash}
$ git push origin experimental
~~~

~~~ {.output}
Counting objects: 5, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 307 bytes, done.
Total 3 (delta 2), reused 0 (delta 0)
To https://github.com/erdavenport/planets.git
 * [new branch]      experimental -> experimental
~~~

Note that in the past we've types `git push origin master` when pushing to our remote.
This was because we were making changes on our `master` branch and pushing to the remote named `origin`.
Here, we've been working on our `experimental` branch. To push those changes to GitHub, we therefore specify that we want to push the `experimental` branch to the remote named `origin`. 

Let's check our status:

~~~ {.bash}
$ git status
~~~

~~~ {.output}
On branch experimental
nothing to commit, working directory clean
~~~

You can see from the git status output that we are on the experimental branch rather than the master branch. Let's examine the master branch to ensure the original version of our `pluto.txt` doesn't include this sentimental statement:

~~~ {.bash}
$ git checkout master
~~~

~~~ {.output}
Switched to branch 'master'
~~~

~~~ {.bash}
$ cat pluto.txt
~~~

~~~ {.output}
It is so a planet!
~~~

As you can see, the master branch does not include our updated notes about Pluto. 
If we look on GitHub, we can switch between the `master` and `experimental` branch and see the same difference between the two versions of `pluto.txt`. 
We are pretty confident that the heart in Pluto is charming, so let's fold in all of the changes that we've made on the experimental branch into our master branch. 
To merge two branches together, ensure you are located in the branch you want to fold changes into. 
In our case, we want to be in the master branch:

~~~ {.bash}
$ git branch
~~~

~~~ {.output}
  experimental
* master
~~~

Excellent, we are in the right place. To fold the experimental branch into the master branch, we use the `merge` function of git followed by the name of the branch we want to fold in:

~~~ {.bash}
$ git merge experimental
~~~

~~~ {.output}
Updating ee530d7..c5d6cba
Fast-forward
 pluto.txt | 1 +
 1 file changed, 1 insertion(+)
~~~

Now if we look at our `pluto.txt` file, we see our updates from the experimental branch:

~~~ {.bash}
$ cat pluto.txt
~~~

~~~ {.output}
It is so a planet!
A planet with a charming heart on its surface; What's not to love?
~~~

Now let's push these changes up to github:

~~~ {.bash}
$ git push origin master
~~~ 

~~~ {.output}
Total 0 (delta 0), reused 0 (delta 0)
To https://github.com/erdavenport/planets.git
   a822910..10ed071  master -> master
~~~

> ## Pushing all branches to GitHub {.callout}
> If you've been working on multiple branches and want to push commits from all branches to GitHub, you can use the following syntax rather than pushing each branch individually:  
>
> `git push --all origin`


Branches can be difficult to visualize in your head. GitHub has a nice feature that will let you examine your commits on each branch. Find the graphs link of your repository home page:

![Locating Graphs on GitHub](fig/github-find-graphs-image.png)  

You can see a graphical representation of your commit and branch history here. If you hover your cursor over the dots (commits), a box will display the commit message and ID. Your different branches are shown in different colors, with an arrow indicating when you merged two branches together.

![Viewing Branch and Commit History on GitHub](fig/github-graphs-image.png)

We no longer have a use for our experimental branch. To delete a branch you don't need, you can use the `-d` flag of `git branch`:

~~~ {.bash}
$ git branch -d experimental
~~~

~~~ {.output}
Deleted branch experimental (was c5d6cba).
~~~

> ## Deleting a remote branch {.callout}
> You've deleted your experimental branch locally, but if you look on your GitHub page, you'll see it still exists, even if you `git push --all origin`. 
> To delete the branch remotely, you should use the syntax:    
>
> `git push origin <local-branch>:<remote-branch>`  
>
> In our example this is: `git push origin experimental:experimental`.
> You can also use the shorthand version: `git push origin :experimental`. 
> Using this notation, Git assumes you are listing the remote branch and want to push the branch you are currently in on the local repo. 
> Essentially you are pushing "nothing" to the remote branch, which erases it.



> ## Creating and Merging Branches {.challenge}
>
> In your `bio` repository you made earlier, do the following:  
> 1. Create a branch called `grad_school`  
> 2. Create a file called `thesis` and write one line about your research (or something about science if you don't know what you'll be researching yet)  
> 3. Merge those changes back to the master branch of `bio`. 

| [⬅ 4. Exploring history](04-exploring-history.md) | [Table of Contents](00-contents.md) |  [6. Setting up a remote repository in GitHub ➡](06-remotes-in-github.md) |
| :---- |:----:| ----:|

# 5. Working with branches

![The Git Staging Area](fig/git-staging-area.png)

Often you may want to test out a new feature in some code. You may or may not decide you want to keep this feature and in the mean time you want to make sure you have a version of your script you know works. Branches are instances of a repository that can be edited and version controlled in parallel. You can think of it like making an entire copy of your repository folder that you can edit, without affecting the original versions of your scripts. The advantage of using git to do this (rather that making a repo_copy folder on your computer), is that you can use git tools to manage this code while it's under development and you have the ability to seamlessly merge in your changes into your originals.

To see what branches are available in your repository, you can type `git branch`. First make sure you're in the planets directory in your home folder:

```
$ cd path-to-planets-dir
$ git branch
* master
```
You see only one branch, "master", which is created when the repository is initialized.

With an argument, the `git branch` command creates a new branch with the given name. Let's make a new experimental branch:

```
$ git branch experimental
  experimental
* master
```

The star indicates we are still currently in the master branch of our repository. To switch branches, we use the `git checkout` command to checkout a different branch. 

```
$ git checkout experimental
Switched to branch 'experimental'
```

Type `git branch` again to see that the star has moved:

```
$ git branch
* experimental
  master
```

Suppose we have some updated information on pluto suggesting it has a heart on its surface, but we aren't sure that we will want to include this detail in our final document. Let's include it in the `pluto.txt` file in our experimental branch:

```
$ vi pluto.txt
$ cat pluto.txt
It is so a planet!
A planet with a charming heart on its surface; What's not to love?
```

We've made this change on our experimental branch. Let's add and commit this change:

```
$ git add pluto.txt
$ git commit -m "Breaking updates about Pluto"
[experimental c5d6cba] Breaking updates about Pluto
 1 file changed, 1 insertion(+)
```

Let's check our status:

```
$ git status
On branch experimental
nothing to commit, working directory clean
```

You can see from the git status output that we are on the experimental branch rather than the master branch. Let's examine the master branch to ensure the original version of our `pluto.txt` doesn't include this sentimental statement:

```
$ git checkout master
Switched to branch 'master'
```

```
$ cat pluto.txt
It is so a planet!
```

As you can see, the master branch does not include our updated notes about Pluto. 

Now we decide we are pretty confident that Pluto's heart is charming, so we want to fold all of the changes we've made on the experimental branch into the master branch. 
To merge two branches together, ensure you are on the branch you want to fold changes *into*. 
In this case, we want to be on the master branch:

```
$ git branch
  experimental
* master
```

Excellent, we are on the right branch. To fold the experimental branch into the master branch, we use the `git merge` command followed by the name of the branch we want to fold *in* to the current branch:

```
$ git merge experimental
Updating ee530d7..c5d6cba
Fast-forward
 pluto.txt | 1 +
 1 file changed, 1 insertion(+)
```

Now if we look at our `pluto.txt` file, we see the updates from the experimental branch in the master branch version:

```
$ cat pluto.txt
It is so a planet!
A planet with a charming heart on its surface; What's not to love?
```

We no longer have a use for our experimental branch. To delete a branch you don't need, you can use the `-d` flag of `git branch`:

```
$ git branch -d experimental
Deleted branch experimental (was c5d6cba).
```

It's possible of course that we may be still trying to decide about some changes but others must be made right away. Suppose we want to list all the co-signers of our treatise on Pluto, but we don't know yet what everyone will contribute so we aren't sure about the order of names. You can be diplomatic and list the whole team in alphabetical order until the final version. 

```
$ git branch
* master
$ vi pluto.txt
$ cat pluto.txt
Co-signers (alphabetical order for now): Dracula, Frankenstein, Mummy, and Wolfman
It is so a planet!
A planet with a charming heart on its surface; What's not to love?
```

Meanwhile, we get some input from Wolfman that we aren't sure about including, so we create a wolfman branch.

```
$ git branch wolfman
$ git checkout wolfman
M       pluto.txt
Switched to branch 'wolfman'
```

The "M" next to pluto.txt reminds us that there is a modified file in the master branch that was never added and committed. Oops! Let's delete the wolfman branch, fix up the master branch, and start over.

```
$ git checkout master
M       pluto.txt
Switched to branch 'master'
$ git branch -d wolfman
Deleted branch wolfman (was 436c68b).
$ git add pluto.txt
$ git commit -m "merged experimental branch into master"
[master b36f548] merged experimental branch into master
 1 file changed, 1 insertion(+)
$ git branch wolfman
$ git checkout wolfman
Switched to branch 'wolfman'
```

Just to be sure, we can type `git status`.

```
$ git status
On branch wolfman
nothing to commit, working tree clean
```

Now we add Wolfman's input and move him up the author list.

```
$ vi pluto.txt
$ cat pluto.txt
Co-signers (alphabetical order for now): Wolfman, Dracula, Frankenstein, Mummy
It is so a planet!
A planet with a heart on its surface; what's not to love?
Technically, Pluto and Charon are a double planet orbiting a center of mass outside either body. However there are several other good moons for howling at.
```

Don't forget to add and commit the changes. You can use the shortcut `-a` to do it in one step.

```
$ git commit -a -m "Wolfman says Pluto and Charon are both planets"
[wolfman c52e999] Wolfman says Pluto and Charon are both planets
 1 file changed, 2 insertions(+), 1 deletion(-)
```

After some discussion with the other co-signers, everyone agrees that it's worth crusading for both Pluto and Charon to be planets. Let's merge the changes into master.

```
$ git checkout master
$ git merge wolfman



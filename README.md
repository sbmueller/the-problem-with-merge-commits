# The Problem with Merge Commits

This repository serves as a small example that should emphasize one issue with
merge commits: A new, unreviewed and untested code state might be automatically
created on the server side.

## Observation

In this repo, let's assume multiple contributors work on an application. The
initial commit `a573d9a` can be seen as an arbitrary long history in this
repository, serving as starting point with a passing CI.
The next commit `e2d24c7`, introduces an extension to the business logic with a
file `main.py` and an extension of the CI to execute this file. Note the CI is
green.
Another contributor works on a feature branch `add-config` to add another file
`foo.cfg` in an unrelated context. This change could be any more complex
change, but let's stay with this simple example. See the pull request for this
feature in
[#3](https://github.com/sbmueller/the-problem-with-merge-commits/pull/3). The
CI is green and the reviewer, not suspecting anything bad, approves the merge.
Lastly, the merge is performed using a **merge commit** `62d49b6`, on `main`
suddenly the CI fails. What happened?

## Explanation

The issue is, that a merge commit introduces a new, unreviewed and untested
code state that has not existed before. At no point in time, the files
`main.py` and `foo.cfg` were simultaneously existing. The first time this
happened was after the automatically created merge commit, only on server side.

Unfortunately, the file `foo.cfg` has a "complex" interplay with the business
logic in `main.py` which could not be observed before.

## How to avoid this

Rather than a merge commit, a fast forward merge should be performed:

```
git merge [branch] --ff-only
```

Among other benefits like a linear history, this avoids unseen code states. If
the changes are incompatible for a fast forward, which just means the target
branch pointer gets moved to the source branch pointer, an error is displayed,
asking the user base their changes of the target branch:

```
git rebase -i main
```

After this command, no parallel changes will exist like in our example above.
The file `main.py` would suddenly exist in the branch `add-config` and the
failure would be detected.

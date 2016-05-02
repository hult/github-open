gh-open
=======

Provided your current working directory is a checked-out github repo
with github as the remote "origin", you can just run

    gh-open

And a web browser will be opened, pointing to

    https://github.com/REPO/tree/BRANCH

Example

    $ git remote -v
    origin  git@github.com:hult/example.git (fetch)
    origin  git@github.com:hult/example.git (push)

    $ git status
    On branch master
    [...]

    $ gh-open
    # Browser is opened with url https://github.com/hult/example/tree/master

import os
import subprocess

REPO_URL = "https://github.com/%(repo)s/tree/%(branch)s"

def run_command(command):
    return subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).communicate()[0]

def repo():
    output = run_command("git remote -v | grep -E '^origin'")
    first_line = output.split("\n", 1)[0]
    repo_url = first_line.split()[1]
    return repo_url.split(":")[1].rsplit(".", 1)[0]

def branch():
    output = run_command("git status --branch")
    first_line = output.split("\n", 1)[0]
    return first_line.split()[-1]

def repo_url(repo, branch):
    return REPO_URL % {"repo": repo, "branch": branch}

def current_repo_url():
    return repo_url(repo(), branch())

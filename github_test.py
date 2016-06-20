import nose.tools as nt
import mock
import github

class TestGithub(object):
    run_command_template = {
        'remote': 'origin\tgit@github.com:%(username)s/%(repo)s.git (fetch)\norigin\tgit@github.com:%(username)s/%(repo)s.git (push)\n',
        'status': 'On branch %(branch)s\nUntracked files: ...'
    }

    def run_command_mock(self, command):
        git_command = command.split(" ")[1]
        return self.run_command_template[git_command] % {
            'username': self.username,
            'repo': self.repo,
            'branch': self.branch
        }

    def setup(self):
        self.username = 'hult'
        self.repo = 'github-open'
        self.branch = 'branch-name'
        github.run_command = self.run_command_mock

    def test_repo(self):
        nt.assert_equals('hult/github-open', github.repo())
        self.repo = 'example.org'
        nt.assert_equals('hult/example.org', github.repo())

    def test_branch(self):
        nt.assert_equals('branch-name', github.branch())
        self.branch = 'branch.name'
        nt.assert_equals('branch.name', github.branch())

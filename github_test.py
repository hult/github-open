import nose.tools as nt
import mock
import github

class TestGithub(object):
    run_command_template = 'origin\tgit@github.com:%(username)s/%(repo)s.git (fetch)\norigin\tgit@github.com:%(username)s/%(repo)s.git (push)\n'

    def run_command_mock(self, command):
        return self.run_command_template % {'username': self.username, 'repo': self.repo}

    def setup(self):
        self.username = 'hult'
        self.repo = 'github-open'
        github.run_command = self.run_command_mock

    def test_repo(self):
        nt.assert_equals('hult/github-open', github.repo())
        self.repo = 'example.org'
        nt.assert_equals('hult/example.org', github.repo())

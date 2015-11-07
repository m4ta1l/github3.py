import github3

from .helper import (UnitHelper, create_example_data_helper, create_url_helper)

get_example_data = create_example_data_helper('tree_example')
url_for = create_url_helper('https://api.github.com/repos/sigmavirus24/github3.py/'
                            'git/trees/75b347329e3fc87ac78895ca1be58daff78872a1')


class TestTree(UnitHelper):
    """Tree unit test"""

    described_class = github3.git.Tree
    example_data = get_example_data()

    def test_repr(self):
        """Assert Tree in in the repr."""
        assert isinstance(self.instance, github3.git.Tree)
        assert repr(self.instance).startswith('<Tree')

    def test_recurse(self):
        """Assert that URL is called"""
        self.instance.recurse()
        self.session.get.assert_called_once_with(
            url_for(),
            params={u'recursive': u'1'}
        )

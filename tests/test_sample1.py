from unittest import TestCase

from sample import sample1


class TestHello(TestCase):
    def test_hello(self):
        s = sample1.hello()
        assert s == 'hello'

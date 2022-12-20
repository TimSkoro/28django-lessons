from django.test import TestCase


class TestSome(TestCase):

    def test_one(self):
        raise ZeroDivisionError

    def test_two(self):
        return False
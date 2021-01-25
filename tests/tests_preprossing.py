from .context import tulipe
from tulipe import preprocessing

import unittest


class TestsPreprocessing(unittest.TestCase):

    def test_preprocessing_fullpath(self):
        words = preprocessing.parse('/home/thales/Dev/Tulipe/tests/sample.pdf')
        self.assertIsNotNone(words)

    def test_preprocessing_relpath(self):
        words = preprocessing.parse('~/Dev/Tulipe/tests/sample.pdf')
        self.assertIsNotNone(words)

    def test_preprocessing_numeric_type(self):
        with self.assertRaises(ValueError):
            preprocessing.parse('blabla/somefile.12093')

    def test_preprocessing_unknown_type(self):
        with self.assertRaises(ValueError):
            preprocessing.parse('~/somefile.pryt')

    def test_preprocessing_more_than_one_word(self):
        words = preprocessing.parse('/home/thales/Dev/Tulipe/tests/sample.pdf')
        self.assertGreater(len(words), 1)

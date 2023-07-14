import unittest
import words

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._dict = words.get_all_words()

    def test_insert(self):
        self.assertEqual(words.insert_letter("a", "bc", []),
                         ["abc", "bac", "bca"])
        self.assertEqual(words.insert_letter("a", "bcd", []),
                         ["abcd", "bacd", "bcad", "bcda"])

    def test_add_words_to_letter(self):
        self.assertEqual(words.add_words_to_letter("a", ["bc", "cb"]), ["abc", "acb"])

    def test_enumeration(self):
        self.assertEqual(set(words.enumerate_possibilities(["c", "a", "t"])),
                         {"cat", "cta", "act", "atc", "tca", "tac"})

    def test_anagrams(self):
        self.assertEqual(words.find_anagrams("cat", self._dict),
                         {"act"})  # add assertion here


if __name__ == '__main__':
    unittest.main()
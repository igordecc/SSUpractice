import unittest
import pair_letter_frequency
from langdetect import detect

class TestPairLetterFrequency(unittest.TestCase):

    def test_all_lower_case(self):
        self.assertTrue(pair_letter_frequency.text.islower())

    def test_chosen_language(self):
        language = detect(pair_letter_frequency.text)
        self.assertEqual(language, pair_letter_frequency.language)

    def test_frequency(self):
        self.assertAlmostEqual(1, sum(pair_letter_frequency.frequency))

        first_element = pair_letter_frequency.frequency[0]
        for second_element in pair_letter_frequency.frequency:
            self.assertLessEqual(second_element, first_element)     # 2nd <= 1st; descending order
            first_element = second_element

    def test_pair_values(self):
        for pair in pair_letter_frequency.dictionary.keys():
            first, second = pair
            self.assertFalse((first is ' ')or(second is ' '))


if __name__ == '__main__':
    unittest.main()
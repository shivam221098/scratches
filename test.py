import unittest
import books


class TestCases(unittest.TestCase):
    def test_merge_method(self):
        dictionary1 = books.Dictionary('English', 'German', 5)
        dictionary2 = books.Dictionary("English", "Spanish", 10)
        dictionary1.add_translation(('apple', 'Apfel'), ('table', 'Tabelle'), ('dog', 'Hund'))
        dictionary2.add_translation(("dog", "perra"), ("apple", "manzana"), ("chair", "silla"))
        german_spanish = books.Dictionary.merge(dictionary1, dictionary2)

        merged_dict = books.Dictionary("German", "Spanish", 5)
        merged_dict.add_translation(('Apfel', "manzana"), ('Hund', "perra"))

        self.assertEqual(str(german_spanish), str(merged_dict))

        english_hungarian = books.Dictionary('English', 'Hungarian', 5)
        english_hungarian.add_translation(('apple', 'alma'), ('table', 'asztal'), ('dog', 'kutya'))
        english_russian = books.Dictionary('English', 'Russian', 8)
        english_russian.add_translation(('apple', 'яблоко'), ('table', 'стол'), ('cat', 'кошка'))
        hungarian_russian = books.Dictionary.merge(english_hungarian, english_russian)

        new_merge = books.Dictionary("Hungarian", "Russian", 5)
        new_merge.add_translation(("alma", "яблоко"), ("asztal", "стол"))
        
        self.assertEqual(str(hungarian_russian), str(new_merge))


if __name__ == '__main__':
    unittest.main()

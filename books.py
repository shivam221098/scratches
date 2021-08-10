class Dictionary:
    def __init__(self, language, target_language, price):
        self.language = language
        self.target_language = target_language
        self.price = price
        self.translations = []

    def add_translation(self, *args):
        for tr in args:
            self.translations.append(tr)

    def __str__(self):
        string = "{} - {} dictionary - {}$\n".format(self.language, self.target_language, self.price)
        for tr in self.translations:
            string += "{} - {}\n".format(tr[0], tr[1])

        return string

    @staticmethod
    def merge(dict1, dict2):
        new_translations = []
        for i in range(len(dict1.translations)):
            for j in range(len(dict2.translations)):
                if dict1.translations[i][0] == dict2.translations[j][0]:
                    new_translations.append((dict1.translations[i][1], dict2.translations[j][1]))

        if dict1.price < dict2.price:
            price = dict1.price

        else:
            price = dict2.price

        dictionary = Dictionary(dict1.target_language, dict2.target_language, price)
        for tr in new_translations:
            dictionary.add_translation(tr)

        return dictionary


class Fiction:
    def __init__(self, title, description, price):
        self.title = title
        self.description = description
        self.price = price

    def __str__(self):
        return "{} - {}$\n{}".format(self.title, self.price, self.description)


class BookPublisher:
    def __init__(self, name):
        self.name = name
        self.published_books = []

    def publish(self, *args):
        for book in args:
            self.published_books.append(book)

    def show_products(self):
        for product in self.published_books:
            print(product)


if __name__ == '__main__':
    english_hungarian = Dictionary('English', 'Hungarian', 5)
    english_hungarian.add_translation(('apple', 'alma'), ('table', 'asztal'), ('dog', 'kutya'))
    english_russian = Dictionary('English', 'Russian', 8)
    english_russian.add_translation(('apple', 'яблоко'), ('table', 'стол'), ('cat', 'кошка'))
    hungarian_russian = Dictionary.merge(english_hungarian, english_russian)

    fiction = Fiction('Nineteen Eighty-Four', 'A science fiction novel by English novelist George Orwell', 10)
    golden_books = BookPublisher('Golden Books')
    golden_books.publish(english_hungarian, english_russian, hungarian_russian, fiction)
    golden_books.show_products()
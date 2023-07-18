import unittest

from dotenv import dotenv_values

from api import Bookworm


class TestBookworm(unittest.TestCase):
    def test_get_text(self):
        config = dotenv_values('../.env')

        with open('resources/wakeupcat.jpg', 'rb') as image_file:
            text = Bookworm(config['api_url']).get_text(image_file)
            assert text
            print(text)
            assert text['locale'] == 'en'
            assert text['description'] == 'Wake up human!'


if __name__ == '__main__':
    unittest.main()

import unittest
from main import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Лабораторная работа №3'.encode('utf-8'), response.data)

    def test_submit(self):
        data = {
            'price': 1000000,
            'initial_fee': 4000000,
            'term': 20,
            'rate': 15
        }
        response = self.app.post('/result', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Лабораторная работа №3'.encode('utf-8'), response.data)


if __name__ == '__main__':
    unittest.main()
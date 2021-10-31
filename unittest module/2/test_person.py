import unittest
from person import Person


class PersonTest(unittest.TestCase):

    def setUp(self):
        self.p1 = Person('mohammadhssn', 'Alizadeh')
        self.p2 = Person('sara', 'ahmadi')

    def test_full_name(self):
        self.assertEqual(self.p1.full_name(), 'mohammadhssn Alizadeh')
        self.assertEqual(self.p2.full_name(), 'sara ahmadi')

    def test_email(self):
        self.assertEqual(self.p1.email(), 'mohammadhssnAlizadeh@email.com')
        self.assertEqual(self.p2.email(), 'saraahmadi@email.com')


if __name__ == '__main__':
    unittest.main()

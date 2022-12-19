import unittest

from person import Person


class PersonTest(unittest.TestCase):
    def setUp(self):
        self.p = Person("hoge", "company", "000", "1234-5678")

    def test_PhoneNumber(self):
        self.assertEqual(self.p.office_telephone_number, "000-1234-5678")


if __name__ == "__main__":
    unittest.main()

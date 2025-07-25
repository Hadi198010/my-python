import unittest
import re

class TestPhoneReplace(unittest.TestCase):
    def test_phone_replacement(self):
        text = "Call me at 09123456789 or at 09351234567."
        pattern = r"09\d{9}"
        replaced = re.sub(pattern, "09xxxxxxxxx", text)
        expected = "Call me at 09xxxxxxxxx or at 09xxxxxxxxx."
        self.assertEqual(replaced, expected)

if __name__ == '__main__':
    unittest.main()


import unittest
from Library import LibraryItem


class TestLibrary(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_2(self):
       lp = LibraryItem("354", "Phantom Tollbooth")
        self.assertIsInstance(lp, LibraryItem)

    def test_3(self):
        lp = LibraryItem("354", "Phantom Tollbooth")
        self.assertEqual(lp._get_checked_out_by, None)


if __name__ == '__main__':
    unittest.main()

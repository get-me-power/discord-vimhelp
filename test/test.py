import unittest
import sys
sys.path.append('../src')
import vimhelp


class TestVimhelp(unittest.TestCase):

    def test_vimhelp_method(self):
        self.assertEqual(0, vimhelp.vimhelp("search")[1])


if __name__ == "__main__":
    unittest.main()

import unittest
import sys
sys.path.append('../src')
import vimhelp


class TestVimhelp(unittest.TestCase):

    def test_vimhelp_exist_word(self):
        self.assertEqual(0, vimhelp.vimhelp("search")[1])

    def test_vimhelp_noexist_word(self):
        self.assertEqual(1, vimhelp.vimhelp("noexists")[1])

if __name__ == "__main__":
    unittest.main()

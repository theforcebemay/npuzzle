import unittest
import os
from Input import Input

maps_folder = 'maps'
test_map = 'test_file.txt'

test_text = ['This is\n', 'test\n', 'file\n']

class TestInputClass(unittest.TestCase):

    def test_output_result(self):
        x = Input(os.path.join(maps_folder, test_map))
        self.assertEqual(x.get_content(), test_text)

if __name__ == '__main__':
    unittest.main()

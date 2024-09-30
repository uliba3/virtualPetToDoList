import unittest

from imageToAscii import Image

class TestImages(unittest.TestCase):
    def test_file_path(self):
        file_path: str = "./vendor/rose.png"
        image: Image = Image(file_path)
        
        self.assertEqual(image.print_file_path(), file_path)
    
    def test_image(self):
        file_path: str = "./vendor/rose.png"
        image: Image = Image(file_path)
        
        self.assertEqual(image.print_image(), file_path)


if __name__ == "__main__":
    unittest.main()
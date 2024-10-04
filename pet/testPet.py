import unittest

from pet import Pet

class PetTesting(unittest.TestCase):
    
    def test_get_walking_image(self):
        
        my_dog = Pet()     
        self.assertEqual(my_dog.get_walking_image(), "Walk")
    
    
    def test_get_barking_image(self):
        
         my_dog = Pet()     
         self.assertEqual(my_dog.get_barking_image(), "Bark")
        
    def test_get_smiling_image(self):
        
         my_dog = Pet()     
         self.assertEqual(my_dog.get_smiling_image(), "Smile")

if __name__ == "__main__":
    unittest.main()
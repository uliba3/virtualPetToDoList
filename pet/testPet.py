import unittest
    
from pet import Pet 

class PetTesting(unittest.TestCase):
    
    def test_get_walking_image(self):
        
        my_dog = Pet()     
        print(my_dog.get_walking_image())
    
    
    def test_get_barking_image(self):
        
         my_dog = Pet()     
         print(my_dog.get_barking_image())
        
    def test_get_smiling_image(self):
        
         my_dog = Pet()     
         
         print(my_dog.get_smiling_image())
    
    def test_get_name(self):
        
        soobin_dog = Pet()
        charlie_dog = Pet("Charlie")
        
        self.assertEqual(soobin_dog.get_name(), "Soobin")
        self.assertEqual(charlie_dog.get_name(), "Charlie")
        

if __name__ == "__main__":
    unittest.main()
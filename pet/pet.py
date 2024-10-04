from imageToAscii import Image

class Pet:
    
    """
    The pet is capable of returning strings that are ASCII images. To use them simply print the returned string to the console.
    Eg.
    ```python
    my_pet = Pet("Charlie")
    print(my_pet.get_walking_image())
    ```
    """
    
    
    def __init__(self, name="Soobin") -> None:
        self.name = name
        self.smiling_dog_image = Image("vendor/similing_dog.png")
        
    def get_name(self) -> str:
        """
        Returns the name of the pet. The default name is Soobin
        """
        return self.name
    
    def get_walking_image(self) -> str:
        """
        Returns a string that looks like the image of a walking dog.
        """
        return "Walk" 
        
    def get_barking_image(self) -> str:
        """
        Returns a string that looks like the image of a barking dog.
        """
        return "Bark" 
    
    def get_smiling_image(self) -> str:
        """
        Returns a string that looks like the image of a smiling dog.
        """
        return self.smiling_dog_image.get_image_string()
    
    def add_event(self, event_details) -> None:
        """
        Add an event to the TODO list with details event_details.
        """
    
    def remove_event(self, event_id) -> None:
        """
        Remove an event that has the identifier event_id
        """
    
    def modify_event(self, event_id, event_details) -> None:
        """
        Replace the details of an event that has the identifier event_id, with event_details
        """
    
    def get_all_event(self) -> None:
        """
        The function returns all the events that have been added to the TODO list
        """
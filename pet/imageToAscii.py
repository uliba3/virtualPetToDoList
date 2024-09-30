

### This module should be able to convert a given image into ascii art 
### Input:
### 1 .Need to know the number of characters that can be printed on the screen
### 2. Need to know what image to print


class Image:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        
    def print_file_path(self) -> str:
        return self.file_path
        
        
    def print_image(self) -> str:
        return self.file_path

#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = 'New'

   
    def size(self):
        return self.__size

    
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("The shoe has been repaired.")
        self.condition = 'New'
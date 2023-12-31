class Square:
    def __init__(self, size=0):
        self.__size = size
    
    def area(self):
        return self.__size ** 2
    
    def size(self):
        return self.__size
    
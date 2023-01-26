from node import Node


class StackPopException(Exception):
    "Raised when occurs an error in stack class .pop() method."
    def __init__(self, message="It's not possible pop from a empty stack."):
        self.message = message
        super().__init__(self.message)


class Stack:
    """Stack implementation without built-in data structures and methods."""

    def __init__(self):
        self.__top = None
        self.__stack_size = 0
        self.add = self.push # Because of tests.py line 37
        self.print = self.__str__ # Because of tests.py lines 64 and 70

    def __len__(self):
        """Returns the stack's size."""
        
        return self.__stack_size
    
    def is_empty(self):
        """Returns if the stack is empty or not."""
        
        return not self.__stack_size

    def push(self, item):
        """Adds a new element on top of the stack.
        
        Parameters
        ----------
            - item (Any): The new item to be added.
        """
        
        new_node = Node(item, self.__top)
        self.__stack_size += 1
        self.__top = new_node

    def pop(self):
        """Deletes the element on top of the stack.
        
        Returns
        -------
            - item (Any): The item deleted.
        """

        if self.is_empty():
            raise StackPopException

        item = self.__top.get_item()
        self.__top = self.__top.get_next_node()
        self.__stack_size -= 1

        return item
    
    def __str__(self):
        """Prints all items of the stack.
        
        Returns
        -------
            - output (str): The stack's items with the form: 1 -> 2 -> 3.
        """

        temp_top = self.__top
        output = ''

        while temp_top is not None:
            item = temp_top.get_item()
            output += str(item) + ' -> '
            temp_top = temp_top.get_next_node()

        if output != '': # Just to remove the last ' -> ' caracteres 
            output = output[0:len(output)-4]

        return output

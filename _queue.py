from node import Node


class QueueDequeueException(Exception):
    "Raised when occurs an error in queue class .dequeue() method."
    def __init__(self, message="It's not possible dequeue from a empty queue."):
        self.message = message
        super().__init__(self.message)


class Queue:
    """Queue implementation without built-in data structures and methods."""

    def __init__(self):
        self.__begin = None
        self.__end = None
        self.__queue_size = 0
        self.print = self.__str__ # Because of tests.py lines 127 and 133
    
    def __len__(self):
        """Returns the queue's size."""
        
        return self.__queue_size
    
    def is_empty(self):
        """Returns if the queue is empty or not."""
        
        return not self.__queue_size

    def enqueue(self, item):
        """Adds a new element to the end of the queue.
        
        Parameters
        ----------
            - item (Any): The new item to be added.
        """

        new_node = Node(item)

        if self.__queue_size == 0:
            self.__begin = self.__end = new_node # Holds the same reference
        else:
            self.__end.set_next_node(new_node)
            self.__end = new_node
        
        self.__queue_size += 1

    def dequeue(self):
        """Deletes the element from the beginning of the queue.
        
        Returns
        -------
            - item (Any): The item deleted.
        """

        if self.is_empty():
            raise QueueDequeueException

        item = self.__begin.get_item()
        self.__begin = self.__begin.get_next_node()
        self.__queue_size -= 1
        if self.__queue_size == 0:
            self.__end = None

        return item
    
    def __str__(self):
        """Prints all items of the queue.
        
        Returns
        -------
            - output (str): The queue's items with the form: 1 -> 2 -> 3.
        """

        temp_begin = self.__begin
        output = ''

        while temp_begin is not None:
            item = temp_begin.get_item()
            output += str(item) + ' -> '
            temp_begin = temp_begin.get_next_node()

        if output != '': # Just to remove the last ' -> ' caracteres 
            output = output[0:len(output)-4]

        return output

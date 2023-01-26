class Node:
    """A element of a stack or queue.

    Parameters
    ----------
        - item (Any): The node's item.
        - next (Node): 'Pointer' for the next node.
    """

    def __init__(self, item, next=None):
        self.__item = item
        self.__next_node = next
    
    def get_item(self):
        """Returns the node's item."""
        
        return self.__item
    
    def get_next_node(self):
        """Returns the next node."""
        
        return self.__next_node
    
    def set_next_node(self, new_node):
        """Sets the next node.
        
        Parameters
        ----------
        - newNode (Node): The new next node.
        """
        
        self.__next_node = new_node

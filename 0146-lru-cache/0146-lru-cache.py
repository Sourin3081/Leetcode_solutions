class Node(object):
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node()   # Least recently used side
        self.right = Node()  # Most recently used side

        self.left.next = self.right
        self.right.prev = self.left


    def remove(self, node):
        """Remove node from linked list"""
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode


    def insert(self, node):
        """Insert node at most recently used position"""
        prevNode = self.right.prev

        prevNode.next = node
        node.prev = prevNode

        node.next = self.right
        self.right.prev = node


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move it to most recently used position
        self.remove(node)
        self.insert(node)

        return node.value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        # If key already exists, remove old node
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]

        # Create new node
        node = Node(key, value)

        self.cache[key] = node
        self.insert(node)

        # Capacity exceeded
        if len(self.cache) > self.capacity:

            # First real node is least recently used
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]
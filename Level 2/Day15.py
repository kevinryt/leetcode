

class MyQueue(object):

    def __init__(self):
        self.push_list = []
        self.pop_list = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.push_list.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        self.swap()
        return self.pop_list.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        self.swap()
        return self.pop_list[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.pop_list) + len(self.push_list) == 0

    def swap(self):
        if len(self.pop_list) == 0:
            while self.push_list:
                self.pop_list.append(self.push_list.pop())

class MinStack(object):

    def __init__(self):
        self.list = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.list:
            cur_min = val
        else:
            cur_min = min(val, cur_min)
        self.list.append((val, cur_min))

    def pop(self):
        """
        :rtype: None
        """
        self.list.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.list[len(self.list)-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.list[len(self.list)-1][1]

class TrieNode:
    def __init__(self):
        self.children = {}
        self.node_end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.node_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.node_end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
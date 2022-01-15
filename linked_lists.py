from logging import root


class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self, root = None , size = 0):
        self.root = root
        self.size = size
    
    def add(self, data):
        self.root = Node(data, self.root)
        self.size += 1
    
    def pop(self, data):
        curr = self.root
        prev = None
        while curr:
            if curr.data == data:
                if prev:
                    prev.next = curr.next
                    return True
                else:
                    self.root = curr.next
                    curr = None
                    return True
            else:
                prev = curr
                curr = curr.next
        return False


    def get_size(self):
        return self.size

    def find(self, data):
        curr = self.root
        prev = None
        while curr:
            if curr.data == data:
                return data
            else:
                prev = curr
                curr = curr.next
        return False

    def print(self):
        curr = self.root
        while curr:
            print(curr.data)
            curr = curr.next

    def reverse(self):
        prev = None
        curr = self.root
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.root = prev
    
    def hasCycle(self):
        tortoise = self.root
        hare = self.root.next

        while tortoise != hare:
            if not hare.next:
                return False
            if not tortoise.next or not hare.next.next:
                return False
            tortoise = tortoise.next
            hare = hare.next.next
        return True


a = LinkedList()
a.add(1)
a.add(3)
a.add(4)
a.reverse()
a.pop(1)
a.print()
print(a.hasCycle())
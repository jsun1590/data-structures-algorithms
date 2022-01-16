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
        while curr:
            if curr.data == data:
                return data
            else:
                curr = curr.next
        return False

    def print(self):
        out = ""
        curr = self.root
        while curr:
            out += str(curr.data) + "->"
            curr = curr.next
        return out.rstrip("->")

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

    def makeCycle(self, index):
        curr_index = 0
        curr = self.root
        while curr.next:
            if curr_index < index:
                curr_index += 1
                ptr = curr
            curr = curr.next
        curr.next = ptr


    
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
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.reverse()
print(a.print())
a.makeCycle(2)
print(a.hasCycle())
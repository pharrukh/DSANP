# Hanoi Tower
class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self, name):
        self.num_elements = 0
        self.head = None
        self.name = name

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0
    
    def __str__(self):
        node = self.head
        string = self.name + '\n'
        while node:
            string += str(node.data) +'\n'
            node = node.next
        return string + '====='

def move(s1, s2):
    #print('---\nleft',s1)
    #print('right',s2, '\n---')
    #print(s1.top(), s2.top())
    if s1.is_empty():
        s1.push(s2.pop())
        print(s2.name, s1.name)
    elif s2.is_empty():
        s2.push(s1.pop())
        print(s1.name, s2.name)
    elif s1.top() > s2.top():
        s1.push(s2.pop())
        print(s2.name, s1.name)
    else:
        s2.push(s1.pop())
        print(s1.name, s2.name)

        
def process_even(s,a,d):
    move(s,a)
    move(s,d)
    move(a,d)

def process_odd(s,a,d, n):
    move(s,d)
    if d.size() == n:
        return
    move(s,a)
    move(a,d)
                
def tower_of_Hanoi(num_disks):
    """
    :param: num_disks - number of disks
    TODO: print the steps required to move all disks from source to destination
    """
    s = Stack('S')
    a = Stack('A')
    d = Stack('D')
    
    for i in reversed(range(1, num_disks + 1)):
        s.push(i)
    #print(s)
    while d.size() != num_disks:
        if num_disks % 2 == 0:
            process_even(s,a,d)
        else:
            process_odd(s,a,d, num_disks)
            
tower_of_Hanoi(4)
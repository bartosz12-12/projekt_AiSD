class Node():
    def __init__(self,value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head =Node()
        self.tail = Node()

    def __len__(self):
        x = self.head
        if self.head.value == None:
            return 0
        wynik = 0
        while x != None:
            x = x.next
            wynik+=1
        return wynik


    def push(self,value):
        x = Node(value)
        if self.head == None:
            self.head = x
        else:
            y = self.head
            x.next = y
            self.head = x



    def append(self, value):
        x = Node(value)
        if self.head.value == None:
            self.head = x
        else:
            y = self.head
            while y.next != None:
                y = y.next
            y.next = x

    def node(self, z):
        if len(self) >= z:
            x = self.head
            for y in range(z):
                x = x.next
            return x



    def remove_last(self):
        x = self.head
        for y in range(len(self)-2):
            x = x.next
        x2 = x.next
        x.next = None
        return x2

    def remove(self,after):
        if self.head.value == None:
            print("lista jest pusta")
            return
        if after >=len(self):
            print("nie ma takiego indeksu")
            return
        x = self.head
        pozycja = 0
        while x.next != None:
            poprzednik = x
            x = x.next
            if pozycja == after - 1:
                poprzednik.next = x.next
                return
            pozycja +=1



    def __str__ (self):
        x = self.head
        llstr = ''
        while x:
            llstr += str(x.value) + " --> "
            x = x.next
        return llstr




    def pop(self):
        x = self.head
        self.head = x.next
        return x

class Stack:
    def __init__(self):
        self.head = LinkedList()

    def push(self, element):
        self.head.push(element)


    def __len__(self):
        return len(self.head)

    def __str__(self):
        llstr = ""
        for x in range(len(self.head)):
            llstr += str(self.head.pop().value) +"\n"

        return(llstr)


    def pop(self):
        return self.head.pop().value

class Queue:
    def __init__(self):
        self.storage = LinkedList()

    def peek(self):
        return self.storage.node(len(self.storage)-1).value

    def enqueue(self,element):
        self.storage.push(element)

    def __len__(self):
        return len(self.storage)

    def dequeue(self):
        return self.storage.remove_last()

    def __str__(self):
        llstr = ""
        for x in range(len(self.storage)):
            llstr += str(self.storage.node(x).value) + ","
        return llstr




# queue = Queue()
# queue.enqueue(2)
# queue.enqueue(4)
# queue.enqueue(5)
# queue.enqueue(6)
# queue.dequeue()
# print(queue.peek())
#
# print(queue)


# stack = Stack()
# stack.push(2)
# stack.push(3)
# stack.push(3)
# stack.pop()
# stack.print()

list=LinkedList()
list.push(1)
list.push(0)
print(list)
assert str(list) == '0 --> 1 --> None --> '
# list.append(6)
# list.append(5)
# list.append(7)
# # print(list.node(2))
# list.push(4)
# list.push(5)
# # list.pop()
# list.remove(2)
# list.__len__()
# list.remove_last()
# # list.remove_last()
# # print(list.node(3))
# # print(list.len())













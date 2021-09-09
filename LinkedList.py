class Node:
    def __init__(self,data= None,next= None,prev= None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList():
    def __init__(self,object= None):
        self.head = Node()
        self.tail= Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

        if object is not None:
            for data in object:
                self.append(data)
    
    def to_node(self,index):
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
        return cur

    def append(self,data):
        cur = self.tail
        cur = cur.prev
        new_node = Node(data,self.tail,cur)
        cur.next = new_node
        self.tail.prev = new_node # gold
        self.size +=1
    
    def pop(self,index=None):
        if self.is_empty():
            raise IndexError
        if index is None:
            cur = self.tail.prev
            data = cur.data
            cur = cur.prev 
            cur.next = self.tail
            self.tail.prev = cur
        else :
            if index < 0 :
                index += self.size
            # traverse
            cur = self.to_node(index)
            data = cur.data
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
        return data

    def is_empty(self):
        return True if self.size == 0 else False
    
    def is_not_empty(self):
        return True if self.size >0 else False

    def __iter__(self):
        cur = self.head
        while cur.next.next != None:
            cur = cur.next
            yield cur.data

    def __str__(self):
        return "[" + ",".join(str(data) for data in self) + "]"

    def __len__(self):
        return self.size

    def __getitem__(self,index):
        if self.is_empty():
            raise IndexError
        while index < 0 :
            index += self.size 
        cur = self.to_node(index)
        return cur.data
    
    def __setitem__(self,index,value):
        if self.is_empty():
            raise IndexError
        while index < 0:
            index += self.size
        cur = self.to_node(index)
        cur.data = value
        return

if __name__ == '__main__':
    a = LinkedList(x for x in range(15))
    print(a)
    a.pop()
    a.pop(2)
    print(a[-1])
class Node:
    data = None
    prev = None
    nextNode = None

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.nextNode = None


class List:
    head = None

    def insert(self, data: int):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            newNode = Node(data)
            track = self.head
            while track.nextNode != None:
                track = track.nextNode
            track.nextNode = newNode
            newNode.prev = track
            return

    def Display(self):
        while self.head:
            print(self.head.data)
            self.head = self.head.nextNode


def recursiveDisplay(node: Node):
    if node == None:
        return
    print(node.data)
    recursiveDisplay(node.nextNode)


def reverseDoublyList(node: Node):
    temp = None
    cur = node
    while cur:
        temp = cur.prev
        cur.prev = cur.nextNode
        cur.nextNode = temp
        cur = cur.prev
    recursiveDisplay(temp.prev)


def deleteHeadNode(node: Node):
    if node is None or node.nextNode is None:
        return None
    node = node.nextNode
    node.prev = None
    recursiveDisplay(node)


def deleteLastNode(node: Node):
    if node is None or node.nextNode is None:
        return None

    cur = node
    while cur.nextNode:
        cur = cur.nextNode

    cur.prev.nextNode = None
    recursiveDisplay(node)


def getLength(node):
    length = 0
    while node:
        length += 1
        node = node.nextNode
    return length


def insertAtN(node: Node, n: int, data: int):
    if node is None:
        return None
    counter = 1
    newNode = Node(data)
    track = node
    if counter is n:
        newNode.nextNode = node
        node.prev = newNode
        recursiveDisplay(newNode)
        return
    while track.nextNode and counter != n - 1:
        track = track.nextNode
        counter += 1
    if counter != n - 1:
        return None
    newNode.prev = track
    newNode.nextNode = track.nextNode
    track.nextNode = newNode
    recursiveDisplay(node)


ob = List()
ob.insert(10)
ob.insert(12)
ob.insert(19)
ob.insert(18)
insertAtN(ob.head, 1, 30)

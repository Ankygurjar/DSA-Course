class Node:
    data = None
    nextNode = None

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkList:
    head = None

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        else:
            node = self.head
            while node and node.nextNode != None:
                node = node.nextNode
            node.nextNode = Node(data)
            return

    def Display(self):
        node = self.head
        while node:
            print(node.data)
            node = node.nextNode


def display(node):
    while node:
        print(node.data)
        node = node.nextNode


def recurSiveDisplay(node: Node):
    if node is None:
        return
    print(node.data)
    recurSiveDisplay(node.nextNode)


def insertAtBegining(node: Node, data: int):
    if node is not None:
        head = Node(data)
        head.nextNode = node
        recurSiveDisplay(head)
        return
    return None


def insertAtEnd(node: Node, data: int):
    if node is not None:
        track = node
        while track.nextNode != None:
            track = track.nextNode
        track.nextNode = Node(data)
        recurSiveDisplay(node)
        return
    return None


def deleteFirstNode(node: Node):
    if node is None:
        return
    temp = node.nextNode
    del node
    recurSiveDisplay(temp)


def deleteLastNode(node: Node):
    if node is None:
        return
    elif node.nextNode is None:
        node = None
        return
    track = node
    while track and track.nextNode and track.nextNode.nextNode != None:
        track = track.nextNode
    track.nextNode = None
    recurSiveDisplay(node)


def getLength(node: Node):
    length = 0
    while node:
        length += 1
        node = node.nextNode
    return length


def insertAtNthPos(node: Node, n: int, data: int):
    counter: int = 0
    track = node
    newNode = Node(data)
    if n == 1:
        newNode.nextNode = node
        recurSiveDisplay(newNode)
        return
    while track and track.nextNode:
        if counter == n - 1:
            break
        counter += 1
        track = track.nextNode
    temp: Node = track.nextNode
    track.nextNode = newNode
    newNode.nextNode = temp
    recurSiveDisplay(node)


def searchLinkList(node: Node, n: int):
    if node is None:
        return -1
    while node:
        if node.data is n:
            return 1
        node = node.nextNode
    return -1


def recursiveSearchLinkList(node: Node, n: int):
    if node is None:
        return -1
    if node.data is n:
        return 1
    return recursiveSearchLinkList(node.nextNode, n)


ob = LinkList()
ob.insert(5)
ob.insert(10)
ob.insert(12)
ob.insert(8)
print(recursiveSearchLinkList(ob.head, 50))

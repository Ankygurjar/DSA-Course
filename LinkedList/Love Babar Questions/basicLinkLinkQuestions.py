




class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Node = None


class LinkList:

    root = None

    def insert(self, data: int) -> None:
        if self.root is None:
            self.root = Node(data)
            return
        else:
            node = Node(data)
            root = self.root
            while root.next != None:
                root = root.next

            root.next = node

    def insertAtBegining(self, data: int) -> None:
        node = Node(data)
        node.next = self.root
        self.display(node)


def display(node):
    while node:
        print(node.data)
        node = node.next


def deleteEle(root: Node, data):
    node: Node = root
    if node.data == data:
        root = root.next
        display(root)
        return
    while node and node.next and node.next.data != data:
        node = node.next

    if node.next != None:
        node.next = node.next.next
        display(root)
    else:
        print("node is not found")


def circularLinkList(root: Node):
    if root is None:
        return
    node: Node = root
    while node.next:
        node = node.next
    node.next = root
    display(root)


l = LinkList()
l.insert(14)
l.insert(12)
l.insert(11)
l.insert(16)
l.insert(12)
l.insert(6)
# display(l.root)
# deleteEle(l.root, 16)
circularLinkList(l.root)
# l.display()
# l.insertAtBegining(0)





















def nthFromEndList(node: Node, n: int):
    if node is None:
        return None
    slow = node
    fast = node
    while n != 0 and fast:
        n -= 1
        fast = fast and fast.nextNode
    if n == 0:
        while fast is not None:
            slow = slow.nextNode
            fast = fast.nextNode
        return slow.data
    return -1
  
  
  
  
  
  
  
  
  
  
  
  

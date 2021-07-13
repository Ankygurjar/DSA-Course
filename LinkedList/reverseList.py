    
    
    
    # ITERATIVE SOLUTION
    def reverseList(self, head):
        nextNode = None
        prev = None
        cur = head
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        return prev
    
    # RECURSIVE SOLUTION
    def reverseList(head):
        return reverse(head, None)
        
    def reverse(node, prev):
        if node is None:
            return prev
        next = node.next
        node.next = prev
        return reverse(next, node)
        
        
        
        
        
        
        
        

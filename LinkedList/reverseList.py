    
    
    
    
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
        
        
        
        
        
        
        
        

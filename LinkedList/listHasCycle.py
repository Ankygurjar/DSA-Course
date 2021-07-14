



def hasCycle(self, head):
        if head == None:
            return False
        slow = head
        fast = head.next
        
        while fast is not None and fast.next is not None:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
      
      
      
      
      
      

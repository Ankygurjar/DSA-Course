




# Method 1

def pallindromeList(head: Node):
    str1 = ""
    slow = head
    fast = head
    while fast and fast.nextNode:
        str1 += str(slow.data)
        slow = slow.nextNode
        fast = fast.nextNode.nextNode

    if fast != None:
        str1 += str(slow.data)
    i = len(str1) - 1
    while slow and i >= 0:
        if slow == None:
            return False
        if slow.data != int(str1[i]):
            return False
        slow = slow.nextNode
        i -= 1
    return True


 # Method 2 By Reversing the half of the given Link List ( More Efficient ) Approach

def isPalindrome(self, head):
        if head == None:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        rev = None
        cur = slow
        while cur:
            next = cur.next
            cur.next = rev
            rev = cur
            cur = next
    
        while head and rev:
            if head.data != rev.data:
                return False
            head = head.next
            rev = rev.next
    
        return True















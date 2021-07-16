





## Inorder Traversal

def inorderTraversal(head: TreeNode):
    if head is None:
      return
    Inorder(head.left)
    print(head.data)
    Inorder(head.right)

   
 # PreOrder Traversal

def PreOrderTraversal(head: TreeNode):
    if head is None:
        return
    print(head.data)
    PreOrderTraversal(head.left)
    PreOrderTraversal(head.right)
   

# PostOrderReaversal
def PostOrderTraversal(head: TreeNode):
    if head is None:
        return
    PostOrderTraversal(head.left)
    PostOrderTraversal(head.right)
    print(head.data)











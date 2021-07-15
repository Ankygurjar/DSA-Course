





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
   
def PostOrederTraversal(head: TreeNode):
    if head is None:
        return
    PostOrederTraversal(head.left)
    PostOrederTraversal(head.right)
    print(head.data)











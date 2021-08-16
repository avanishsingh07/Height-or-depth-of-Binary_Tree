
def height(root):
    if root==None:
        return -1
    else:
        l_height = height(root.left)
        r_height = height(root.right)
        if (l_height > r_height):
            return 1 + l_height
        else:
            return 1 + r_height
            
            
   #OR-------------------
   
   def height(root):
    if root==None:
        return -1
    else:
    return 1 + max(height(root.left),height(root.right))
    

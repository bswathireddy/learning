'''Importing os and reto get input files and to match the input statements respectively.'''
'''Big O Notation of P10 overall is O(N).'''
import os
import re
'''Defined Function to get input files named ta*.dat and calling function which reads file. '''
'''Big O Notation of getinputfiles function is O(n)'''
def getinputFiles():
    for file in os.listdir("."):
        if file.startswith("ta") and file.endswith(".dat"):
            try:
                if os.path.getsize(file)==None:
                    raise TypeError("File is Empty")
                else:
                    print(file,":")
                    readfile(file)
            except Exception as err:
                print("Error: "+file,err)

'''Defined function to read lines of input files.'''
'''Big O Notation is O(n).'''
def readfile(filepath):
    with open(filepath) as f:
        lines=f.readlines()
        if len(lines)!=2:
            print("Invalid Input")
        match1=re.match("^[\s]*([a-zA-Z]+)[\s]*",lines[0])
        match2=re.match("^[\s]*([a-zA-Z]+)[\s]*", lines[1])
        if match1:
            preorder_line = match1.group(1)
        if match2:
            inorder_line = match2.group(1)
        length=len(inorder_line)
        root=buildTree(inorder_line,preorder_line)
        serializedValue = serialize(root)
        deserializedValue = deserialize(serializedValue)
        inorder_value = inorderTraversal(root)
        preorder_value = preorderTraversal(root)
        postorderValue = postorderTraversal(root)
        r=''
        for k in postorderValue:
            if not k.isspace():
                r = r + k
        print("Result :")
        print(r)
        print("-------------")

class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
'''Serializing and Deserializing Binary Tree. '''
'''Big O Notation of this serializing and deserializing is O(n).'''
node=Node('root',Node('left',Node('left.left')),Node('right'))
s=''
def serialize(node,s=''):
    if(not node):
        s+= "#"
        return s
    s+=(str(node.data)+" ")
    s=serialize(node.left, s=s)
    s=serialize(node.right,s=s)
    return s
l=0
def deserialize(s):
    global l
    if s[l]=="#":
        if(l<len(s)-2):
            l+=2
        return None
    else:
        space=s[l:].find(" ")
        sp=space+l
        node = Node(s[l:sp])
        l=sp+1
        node.left=deserialize(s)
        node.right=deserialize(s)
        return node
'''Inorder Traversal Method.'''
'''Big O Notation is O(1)'''
def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.left)
    inorderTraversal(root.right)
'''Preorder Traversal Method.'''
'''Big O Notation is O(1)'''
def preorderTraversal(root):
    if root is None:
        return
    preorderTraversal(root.left)
    preorderTraversal(root.right)
'''Method to build tree.'''
'''Big O Notation is O(1).'''
def build(first, last, preorder, preorder_index, dict):
    if first>last:
        return None,preorder_index
    root=Node(preorder[preorder_index])
    preorder_index=preorder_index + 1
    index=dict[root.data]
    root.left,preorder_index=build(first,index-1,preorder,preorder_index,dict)
    root.right,preorder_index=build(index+1,last,preorder,preorder_index,dict)
    return root,preorder_index
'''Method to check postorder Traversal. To know that my code is Correct.'''
def postorderTraversal(root):
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        postorder.append(node.data)
    postorder=[]
    dfs(root)
    return postorder
'''Function to build a binary tree.'''
'''Big O Notation of this function is O(n)'''
def buildTree(inorder,preorder):
    dict = {}
    for i, j in enumerate(inorder):
        dict[j] = i
    preorder_index = 0
    return build(0,len(inorder)-1,preorder,preorder_index,dict)[0]


getinputFiles()

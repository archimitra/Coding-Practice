from queue import Queue

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class TreeTraversal:
    def __init__(self):
        self.root = None

    def create_bst(self, values):
        values.sort()
        print(values)
        self.root = self.bst_creator(values)
        return self.root

    def bst_creator(self, values):
        if not values:
            return
        if len(values) == 1:
            return TreeNode(values[0])
        
        mid = len(values) // 2 # [4] [2] [1]
        node = TreeNode(values[mid]) # 5 3 2
        node.left = self.bst_creator(values[:mid]) # [1,2,3,4] [1, 2]
        node.right = self.bst_creator(values[mid+1:]) # [3]  [5,6,7]
        return node

    def traverse(self, type='bfs'):
        if type == 'inorder':
            self.inorder_traversal(self.root)
        elif type == 'preorder':
            self.preorder_traversal(self.root)
        elif type == 'postorder':
            self.postorder_traversal(self.root)
        elif type == 'bfs':
            self.bfs(self.root)

    def bfs(self, node):
        if node is None:
            return
        q = Queue()
        q.put(node)
        while q.qsize() > 0:
            node = q.get()
            print(node.value)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

    def preorder_traversal(self, node=None):
        if node:
            print(node.value)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node=None):
        if node:
            self.inorder_traversal(node.left)
            print(node.value)
            self.inorder_traversal(node.right)        
    
    def postorder_traversal(self, node=None):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)            
            print(node.value)


if __name__ == '__main__':
    t = TreeTraversal()
    a = [1,2,3,4,5,6,7,8]
    root = t.create_bst(a)
    print('BFS')
    t.traverse()
    print('DFS-preorder')
    t.traverse('preorder')
    print('DFS-inorder')
    t.traverse('inorder')
    print('DFS-postorder')
    t.traverse('postorder')

    
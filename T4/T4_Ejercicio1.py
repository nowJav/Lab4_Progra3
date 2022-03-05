class Node:

    def __init__(self, info):  # clase constructor

        self.info = info  
        self.left = None  
        self.right = None  
        self.level = None  

    def __str__(self):

        return str(self.info)  # regrese string


class searchtree:

    def __init__(self):  # clase constructor

        self.root = None

    def create(self, val):  # nodos arbol binario de busqueda

        if self.root == None:

            self.root = Node(val)

        else:

            current = self.root

            while 1:

                if val < current.info:

                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break

                elif val > current.info:

                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break

                else:
                    break

    def bft(self):  # Arbol binario

        self.root.level = 0
        queue = [self.root]
        out = []
        current_level = self.root.level

        while len(queue) > 0:

            current_node = queue.pop(0)

            if current_node.level > current_level:
                current_level += 1
                out.append("\n")

            out.append(str(current_node.info) + " ")

            if current_node.left:

                current_node.left.level = current_level + 1
                queue.append(current_node.left)

            if current_node.right:

                current_node.right.level = current_level + 1
                queue.append(current_node.right)

        print("".join(out))

    def inorder(self, node):

        if node is not None:

            self.inorder(node.left)
            print(node.info)
            self.inorder(node.right)


'''
      def preorder(self,node):
            
           if node is not None:
              
              print (node.info)
              self.preorder(node.left)
              self.preorder(node.right)


      def postorder(self,node):
            
           if node is not None:
              
              self.postorder(node.left)
              self.postorder(node.right)
              print (node.info)
'''

tree = searchtree()
arr = [4, 2, 1, 3, 6, 5, 7]
for i in arr:
    tree.create(i)
print('Arbol Binario')
tree.bft()
print('Inorder Recorrido')
tree.inorder(tree.root)
